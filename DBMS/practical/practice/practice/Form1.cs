using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.Common;
using System.Data.Odbc;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practice
{
    public partial class Form1 : Form
    {
        // connection to the Microsoft SQL Server database
        private SqlConnection dbConnection;

        // instances used to fill the dataset with data from the DB
        private SqlDataAdapter daUsers, daPosts;

        // in-memory cache of data retrieved from a DB
        private DataSet tableData;

        // instance which defines the relationship betweenthe two tables
        private DataRelation drUsersPosts;

        // bindig sources used to bind controls in a user interface to the dataset
        BindingSource bsUsers, bsPosts;

        public Form1()
        {
            InitializeComponent();
        }

        private void ReloadPostsTableView()
        {
            // check if the dataset contains the table 'Posts'
            // if it does, clear the data from it
            if (tableData.Tables["Posts"] != null)
            {
                tableData.Tables["Posts"].Clear();
            }
            // populate the 'Posts' table
            daPosts.Fill(tableData, "Posts");
            PostsView.DataSource = bsPosts;
        }

        // This function is called when the selection changes in the UI that shows data about dancers
        private void UsersView_SelectionChanged(object sender, EventArgs e)
        {
            PostIdText.Clear();
            UserIdText.Clear();
            DateOfPostText.Clear();
            ContentText.Clear();
            ShareCountText.Clear();

            // if at least one row is selected in UsersView, then retrieve the first selected row
            if (UsersView.SelectedRows.Count != 0)
            {
                DataGridViewRow selectedRow = UsersView.SelectedRows[0];

                // create a new sql command that selects all rows from Posts, which are related to the selected User
                daPosts.SelectCommand = new SqlCommand("SELECT * FROM Posts WHERE userId = " + selectedRow.Cells[0].Value, dbConnection);

                // update the Posts table
                ReloadPostsTableView();
            }
        }

        // This function is called when the selection changes in the UI that displays thata about Posts
        private void PostsView_SelectionChanged(object sender, EventArgs e)
        {
            // if at least one post is selected 
            if (PostsView.SelectedRows.Count != 0)
            {
                // retrieve the first row from the selection
                DataGridViewRow selectedRow = PostsView.SelectedRows[0];

                // convert all selected values to strings
                PostIdText.Text = selectedRow.Cells[0].Value.ToString();
                UserIdText.Text = selectedRow.Cells[1].Value.ToString();
                DateOfPostText.Text = selectedRow.Cells[2].Value.ToString();
                ContentText.Text = selectedRow.Cells[3].Value.ToString();
                ShareCountText.Text = selectedRow.Cells[4].Value.ToString();
            }
        }

        // Function called when a post is added
        private void addButton_Click(object sender, EventArgs e)
        {
            // create sql command to insert a new costume in the DB
            SqlCommand command = new SqlCommand("INSERT INTO Posts (postId, userId, dateOfPost, content, shareCount) " +
                "VALUES (@PostID, @UserID, @DateOfPost, @Content, @ShareCount)", dbConnection);
            // if the costume was given an ID
            if (PostIdText.Text.Length != 0)
            {
                try
                {
                    int post_id = Int32.Parse(PostIdText.Text);
                    // if the user id is not empty
                    if (UserIdText.Text.Length != 0)
                    {
                        int user_id = Int32.Parse(UserIdText.Text);
                        char content1;
                        // the size is not mandatory
                        if (UserIdText.Text.Length != 0)
                            content1 = Char.Parse(UserIdText.Text);
                        else
                            content1 = '\0';

                        // add parameters to the previously declared command
                        command.Parameters.Add("@PostID", SqlDbType.Int);
                        command.Parameters["@PostID"].Value = post_id;

                        command.Parameters.Add("@UserID", SqlDbType.Int);
                        command.Parameters["@UserID"].Value = user_id;

                        command.Parameters.Add("@DateOfPost", SqlDbType.Date);
                        command.Parameters["@DateOfPost"].Value = DateOfPostText.Text;

                        command.Parameters.Add("@Content", SqlDbType.VarChar, 2);
                        command.Parameters["@Content"].Value = ContentText.Text;

                        command.Parameters.Add("@ShareCount", SqlDbType.VarChar, 2);
                        command.Parameters["@ShareCount"].Value = ShareCountText.Text;

                        // attempt to insert the new row into the Posts table
                        try
                        {
                            daPosts.InsertCommand = command;
                            daPosts.InsertCommand.ExecuteNonQuery();
                            ReloadPostsTableView();
                        }

                        // error messages
                        catch (SqlException sqlException)
                        {
                            if (sqlException.Number == 2627)
                                MessageBox.Show("The post id must be unique!");
                            else if (sqlException.Number == 547)
                                MessageBox.Show("There's no user with the given id!");
                            else
                                MessageBox.Show(sqlException.Message);
                        }
                    }
                    else
                        MessageBox.Show("Please provide a user id!");
                }
                catch (FormatException ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
            else
                MessageBox.Show("Please provide a post id!");
        }

        // Function called when a post is removed
        private void removeButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("DELETE FROM Posts WHERE postId = @PostID", dbConnection);
            if (PostIdText.Text.Length != 0)
            {
                int post_id = Int32.Parse(PostIdText.Text);
                command.Parameters.Add("@PostID", SqlDbType.Int);
                command.Parameters["@PostID"].Value = post_id;
                try
                {
                    daPosts.DeleteCommand = command;
                    int numberOfDeletedCostumes = daPosts.DeleteCommand.ExecuteNonQuery();
                    if (numberOfDeletedCostumes == 0)
                    {
                        MessageBox.Show("There is no post with the given id!");
                    }
                    else
                    {
                        ReloadPostsTableView();
                    }
                }
                catch (SqlException sqlException)
                {
                    MessageBox.Show(sqlException.ToString());
                }
            }
            else
                MessageBox.Show("Please provide a post id!");
        }

        private void UsersView_DataError(object sender, DataGridViewDataErrorEventArgs e)
        {
            if (e.Exception is InvalidConstraintException)
                MessageBox.Show("The user id you provided does not exist!");
            else if (e.Exception is FormatException)
                MessageBox.Show(e.Exception.Message);
            else
                try
                {
                    throw e.Exception;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                }
        }

        // Function called when a post is updated
        private void updateButton_Click(object sender, EventArgs e)
        {
            SqlCommandBuilder builder = new SqlCommandBuilder(daPosts);
            daPosts.UpdateCommand = builder.GetUpdateCommand();
            try
            {
                daPosts.Update(tableData, "Posts");
            }
            catch (SqlException sqlException)
            {
                if (sqlException.Number == 2627)
                    MessageBox.Show("The post id must be unique!");
                else if (sqlException.Number == 547)
                    MessageBox.Show("There's no user with the given id!");
                else
                    MessageBox.Show(sqlException.Message);
            }
            ReloadPostsTableView();
        }

        // Function to load the form
        private void Form1_Load(object sender, EventArgs e)
        {
            // object to connect to the DB
            dbConnection = new SqlConnection("Server=SCO11;Database=PracticalExam;Trusted_Connection=true");
            dbConnection.Open();

            // data adapter to fetch data from 'Dancer'
            daUsers = new SqlDataAdapter("SELECT * FROM Users", dbConnection);
            tableData = new DataSet();
            daUsers.Fill(tableData, "Users");
            UsersView.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            // data adapter to fetch data from 'Costume'
            daPosts = new SqlDataAdapter("SELECT * FROM Posts", dbConnection);
            daPosts.Fill(tableData, "Posts");
            PostsView.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            // 
            DataColumn userIdPosts = tableData.Tables["Users"].Columns["userId"];
            DataColumn userIdUsers = tableData.Tables["Posts"].Columns["userId"];
            drUsersPosts = new DataRelation("FK_USERS_POSTS", userIdPosts, userIdUsers);
            tableData.Relations.Add(drUsersPosts);

            // binding sources to provide a layer of abstraction between the data and UI
            bsUsers = new BindingSource();
            bsUsers.DataSource = tableData;
            bsUsers.DataMember = "Users";

            bsPosts = new BindingSource();
            bsPosts.DataSource = bsUsers;
            bsPosts.DataMember = "FK_USERS_POSTS";
            UsersView.DataSource = bsUsers;
        }

    }
}
