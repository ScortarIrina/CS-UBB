namespace practice
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.UsersView = new System.Windows.Forms.DataGridView();
            this.PostsView = new System.Windows.Forms.DataGridView();
            this.UsersLabel = new System.Windows.Forms.Label();
            this.PostsLabel = new System.Windows.Forms.Label();
            this.UserIdLabel = new System.Windows.Forms.Label();
            this.PostIdLabel = new System.Windows.Forms.Label();
            this.DateOfPostLabel = new System.Windows.Forms.Label();
            this.ShareCountLabel = new System.Windows.Forms.Label();
            this.ContentLabel = new System.Windows.Forms.Label();
            this.PostIdText = new System.Windows.Forms.TextBox();
            this.UserIdText = new System.Windows.Forms.TextBox();
            this.DateOfPostText = new System.Windows.Forms.TextBox();
            this.ShareCountText = new System.Windows.Forms.TextBox();
            this.ContentText = new System.Windows.Forms.TextBox();
            this.addButton = new System.Windows.Forms.Button();
            this.removeButton = new System.Windows.Forms.Button();
            this.updateButton = new System.Windows.Forms.Button();
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.tableLayoutPanel2 = new System.Windows.Forms.TableLayoutPanel();
            this.tableLayoutPanel3 = new System.Windows.Forms.TableLayoutPanel();
            ((System.ComponentModel.ISupportInitialize)(this.UsersView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.PostsView)).BeginInit();
            this.tableLayoutPanel1.SuspendLayout();
            this.tableLayoutPanel2.SuspendLayout();
            this.tableLayoutPanel3.SuspendLayout();
            this.SuspendLayout();
            // 
            // UsersView
            // 
            this.UsersView.AllowUserToAddRows = false;
            this.UsersView.AllowUserToDeleteRows = false;
            this.UsersView.BackgroundColor = System.Drawing.Color.Snow;
            this.UsersView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.UsersView.Dock = System.Windows.Forms.DockStyle.Fill;
            this.UsersView.Location = new System.Drawing.Point(3, 27);
            this.UsersView.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.UsersView.Name = "UsersView";
            this.UsersView.ReadOnly = true;
            this.UsersView.RowHeadersWidth = 51;
            this.UsersView.RowTemplate.Height = 24;
            this.UsersView.Size = new System.Drawing.Size(748, 441);
            this.UsersView.TabIndex = 0;
            this.UsersView.SelectionChanged += new System.EventHandler(this.UsersView_SelectionChanged);
            // 
            // PostsView
            // 
            this.PostsView.AllowUserToAddRows = false;
            this.PostsView.AllowUserToDeleteRows = false;
            this.PostsView.BackgroundColor = System.Drawing.Color.Snow;
            this.PostsView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.PostsView.Dock = System.Windows.Forms.DockStyle.Fill;
            this.PostsView.Location = new System.Drawing.Point(757, 27);
            this.PostsView.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.PostsView.Name = "PostsView";
            this.PostsView.RowHeadersWidth = 51;
            this.PostsView.RowTemplate.Height = 24;
            this.PostsView.Size = new System.Drawing.Size(804, 441);
            this.PostsView.TabIndex = 1;
            this.PostsView.DataError += new System.Windows.Forms.DataGridViewDataErrorEventHandler(this.UsersView_DataError);
            this.PostsView.SelectionChanged += new System.EventHandler(this.PostsView_SelectionChanged);
            // 
            // UsersLabel
            // 
            this.UsersLabel.AutoSize = true;
            this.UsersLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.UsersLabel.Font = new System.Drawing.Font("Microsoft YaHei UI", 10.8F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.UsersLabel.Location = new System.Drawing.Point(3, 0);
            this.UsersLabel.Name = "UsersLabel";
            this.UsersLabel.Size = new System.Drawing.Size(748, 25);
            this.UsersLabel.TabIndex = 2;
            this.UsersLabel.Text = "Users";
            this.UsersLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // PostsLabel
            // 
            this.PostsLabel.AutoSize = true;
            this.PostsLabel.BackColor = System.Drawing.Color.PaleTurquoise;
            this.PostsLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.PostsLabel.Font = new System.Drawing.Font("Microsoft YaHei UI", 10.8F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PostsLabel.Location = new System.Drawing.Point(757, 0);
            this.PostsLabel.Name = "PostsLabel";
            this.PostsLabel.Size = new System.Drawing.Size(804, 25);
            this.PostsLabel.TabIndex = 3;
            this.PostsLabel.Text = "Posts";
            this.PostsLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // UserIdLabel
            // 
            this.UserIdLabel.AutoSize = true;
            this.UserIdLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.UserIdLabel.Font = new System.Drawing.Font("Microsoft YaHei", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.UserIdLabel.Location = new System.Drawing.Point(3, 43);
            this.UserIdLabel.Name = "UserIdLabel";
            this.UserIdLabel.Padding = new System.Windows.Forms.Padding(10);
            this.UserIdLabel.Size = new System.Drawing.Size(181, 43);
            this.UserIdLabel.TabIndex = 5;
            this.UserIdLabel.Text = "User ID:";
            // 
            // PostIdLabel
            // 
            this.PostIdLabel.AutoSize = true;
            this.PostIdLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.PostIdLabel.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PostIdLabel.Location = new System.Drawing.Point(3, 0);
            this.PostIdLabel.Name = "PostIdLabel";
            this.PostIdLabel.Padding = new System.Windows.Forms.Padding(10);
            this.PostIdLabel.Size = new System.Drawing.Size(181, 43);
            this.PostIdLabel.TabIndex = 4;
            this.PostIdLabel.Text = "Post ID:";
            // 
            // DateOfPostLabel
            // 
            this.DateOfPostLabel.AutoSize = true;
            this.DateOfPostLabel.Dock = System.Windows.Forms.DockStyle.Left;
            this.DateOfPostLabel.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DateOfPostLabel.Location = new System.Drawing.Point(3, 86);
            this.DateOfPostLabel.Name = "DateOfPostLabel";
            this.DateOfPostLabel.Padding = new System.Windows.Forms.Padding(10);
            this.DateOfPostLabel.Size = new System.Drawing.Size(128, 43);
            this.DateOfPostLabel.TabIndex = 6;
            this.DateOfPostLabel.Text = "Date Of Post:";
            // 
            // ShareCountLabel
            // 
            this.ShareCountLabel.AutoSize = true;
            this.ShareCountLabel.Dock = System.Windows.Forms.DockStyle.Left;
            this.ShareCountLabel.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ShareCountLabel.Location = new System.Drawing.Point(3, 172);
            this.ShareCountLabel.Name = "ShareCountLabel";
            this.ShareCountLabel.Padding = new System.Windows.Forms.Padding(10);
            this.ShareCountLabel.Size = new System.Drawing.Size(124, 46);
            this.ShareCountLabel.TabIndex = 6;
            this.ShareCountLabel.Text = "Share count:";
            // 
            // ContentLabel
            // 
            this.ContentLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ContentLabel.Location = new System.Drawing.Point(3, 129);
            this.ContentLabel.Name = "ContentLabel";
            this.ContentLabel.Padding = new System.Windows.Forms.Padding(10);
            this.ContentLabel.Size = new System.Drawing.Size(112, 43);
            this.ContentLabel.TabIndex = 15;
            this.ContentLabel.Text = "Content:";
            // 
            // PostIdText
            // 
            this.PostIdText.Cursor = System.Windows.Forms.Cursors.Hand;
            this.PostIdText.Dock = System.Windows.Forms.DockStyle.Left;
            this.PostIdText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PostIdText.Location = new System.Drawing.Point(190, 2);
            this.PostIdText.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.PostIdText.Multiline = true;
            this.PostIdText.Name = "PostIdText";
            this.PostIdText.Size = new System.Drawing.Size(555, 39);
            this.PostIdText.TabIndex = 11;
            // 
            // UserIdText
            // 
            this.UserIdText.Dock = System.Windows.Forms.DockStyle.Left;
            this.UserIdText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.UserIdText.Location = new System.Drawing.Point(190, 45);
            this.UserIdText.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.UserIdText.Multiline = true;
            this.UserIdText.Name = "UserIdText";
            this.UserIdText.Size = new System.Drawing.Size(555, 39);
            this.UserIdText.TabIndex = 13;
            // 
            // DateOfPostText
            // 
            this.DateOfPostText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DateOfPostText.Location = new System.Drawing.Point(190, 89);
            this.DateOfPostText.Name = "DateOfPostText";
            this.DateOfPostText.Size = new System.Drawing.Size(555, 27);
            this.DateOfPostText.TabIndex = 14;
            // 
            // ShareCountText
            // 
            this.ShareCountText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ShareCountText.Location = new System.Drawing.Point(190, 175);
            this.ShareCountText.Name = "ShareCountText";
            this.ShareCountText.Size = new System.Drawing.Size(555, 27);
            this.ShareCountText.TabIndex = 18;
            // 
            // ContentText
            // 
            this.ContentText.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ContentText.Location = new System.Drawing.Point(190, 132);
            this.ContentText.Name = "ContentText";
            this.ContentText.Size = new System.Drawing.Size(555, 27);
            this.ContentText.TabIndex = 16;
            // 
            // addButton
            // 
            this.addButton.AutoSize = true;
            this.addButton.BackColor = System.Drawing.Color.Transparent;
            this.addButton.FlatAppearance.BorderColor = System.Drawing.Color.RosyBrown;
            this.addButton.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.addButton.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.addButton.Location = new System.Drawing.Point(3, 2);
            this.addButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.addButton.Name = "addButton";
            this.addButton.Padding = new System.Windows.Forms.Padding(20, 0, 0, 0);
            this.addButton.Size = new System.Drawing.Size(172, 50);
            this.addButton.TabIndex = 20;
            this.addButton.Text = "Add Post";
            this.addButton.UseVisualStyleBackColor = false;
            this.addButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // removeButton
            // 
            this.removeButton.AutoSize = true;
            this.removeButton.BackColor = System.Drawing.Color.Transparent;
            this.removeButton.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.removeButton.Location = new System.Drawing.Point(3, 56);
            this.removeButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.removeButton.Name = "removeButton";
            this.removeButton.Padding = new System.Windows.Forms.Padding(20, 0, 0, 0);
            this.removeButton.Size = new System.Drawing.Size(172, 50);
            this.removeButton.TabIndex = 21;
            this.removeButton.Text = "Remove Post";
            this.removeButton.UseVisualStyleBackColor = false;
            this.removeButton.Click += new System.EventHandler(this.removeButton_Click);
            // 
            // updateButton
            // 
            this.updateButton.AutoSize = true;
            this.updateButton.BackColor = System.Drawing.Color.Transparent;
            this.updateButton.FlatAppearance.BorderColor = System.Drawing.Color.Blue;
            this.updateButton.FlatAppearance.BorderSize = 4;
            this.updateButton.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.updateButton.Location = new System.Drawing.Point(3, 110);
            this.updateButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.updateButton.Name = "updateButton";
            this.updateButton.Padding = new System.Windows.Forms.Padding(20, 0, 0, 0);
            this.updateButton.Size = new System.Drawing.Size(172, 50);
            this.updateButton.TabIndex = 22;
            this.updateButton.Text = "Update Post";
            this.updateButton.UseVisualStyleBackColor = false;
            this.updateButton.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.ColumnCount = 2;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 48.20972F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 51.79028F));
            this.tableLayoutPanel1.Controls.Add(this.UsersLabel, 0, 0);
            this.tableLayoutPanel1.Controls.Add(this.PostsLabel, 1, 0);
            this.tableLayoutPanel1.Controls.Add(this.UsersView, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.PostsView, 1, 1);
            this.tableLayoutPanel1.Controls.Add(this.tableLayoutPanel2, 0, 2);
            this.tableLayoutPanel1.Controls.Add(this.tableLayoutPanel3, 1, 2);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(5, 5);
            this.tableLayoutPanel1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 3;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(1564, 692);
            this.tableLayoutPanel1.TabIndex = 23;
            // 
            // tableLayoutPanel2
            // 
            this.tableLayoutPanel2.ColumnCount = 2;
            this.tableLayoutPanel2.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 25F));
            this.tableLayoutPanel2.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 75F));
            this.tableLayoutPanel2.Controls.Add(this.PostIdLabel, 0, 0);
            this.tableLayoutPanel2.Controls.Add(this.PostIdText, 1, 0);
            this.tableLayoutPanel2.Controls.Add(this.UserIdLabel, 0, 1);
            this.tableLayoutPanel2.Controls.Add(this.UserIdText, 1, 1);
            this.tableLayoutPanel2.Controls.Add(this.DateOfPostLabel, 0, 2);
            this.tableLayoutPanel2.Controls.Add(this.DateOfPostText, 1, 2);
            this.tableLayoutPanel2.Controls.Add(this.ContentLabel, 0, 3);
            this.tableLayoutPanel2.Controls.Add(this.ContentText, 1, 3);
            this.tableLayoutPanel2.Controls.Add(this.ShareCountLabel, 0, 4);
            this.tableLayoutPanel2.Controls.Add(this.ShareCountText, 1, 4);
            this.tableLayoutPanel2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel2.Location = new System.Drawing.Point(3, 472);
            this.tableLayoutPanel2.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tableLayoutPanel2.Name = "tableLayoutPanel2";
            this.tableLayoutPanel2.RowCount = 5;
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel2.Size = new System.Drawing.Size(748, 218);
            this.tableLayoutPanel2.TabIndex = 4;
            // 
            // tableLayoutPanel3
            // 
            this.tableLayoutPanel3.ColumnCount = 1;
            this.tableLayoutPanel3.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.tableLayoutPanel3.Controls.Add(this.updateButton, 0, 2);
            this.tableLayoutPanel3.Controls.Add(this.addButton, 0, 0);
            this.tableLayoutPanel3.Controls.Add(this.removeButton, 0, 1);
            this.tableLayoutPanel3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel3.Location = new System.Drawing.Point(757, 472);
            this.tableLayoutPanel3.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tableLayoutPanel3.Name = "tableLayoutPanel3";
            this.tableLayoutPanel3.RowCount = 3;
            this.tableLayoutPanel3.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel3.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel3.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tableLayoutPanel3.Size = new System.Drawing.Size(804, 218);
            this.tableLayoutPanel3.TabIndex = 5;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoScroll = true;
            this.BackColor = System.Drawing.Color.PaleTurquoise;
            this.ClientSize = new System.Drawing.Size(1574, 702);
            this.Controls.Add(this.tableLayoutPanel1);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "Form1";
            this.Padding = new System.Windows.Forms.Padding(5);
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.UsersView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.PostsView)).EndInit();
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            this.tableLayoutPanel2.ResumeLayout(false);
            this.tableLayoutPanel2.PerformLayout();
            this.tableLayoutPanel3.ResumeLayout(false);
            this.tableLayoutPanel3.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView UsersView;
        private System.Windows.Forms.DataGridView PostsView;

        private System.Windows.Forms.Label UsersLabel;
        private System.Windows.Forms.Label PostsLabel;

        private System.Windows.Forms.Label PostIdLabel;
        private System.Windows.Forms.TextBox PostIdText;

        private System.Windows.Forms.Label UserIdLabel;
        private System.Windows.Forms.TextBox UserIdText;

        private System.Windows.Forms.Label DateOfPostLabel;
        private System.Windows.Forms.TextBox DateOfPostText;

        private System.Windows.Forms.Label ContentLabel;
        private System.Windows.Forms.TextBox ContentText;

        private System.Windows.Forms.Label ShareCountLabel;
        private System.Windows.Forms.TextBox ShareCountText;

        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button removeButton;
        private System.Windows.Forms.Button updateButton;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel2;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel3;
    }
}

