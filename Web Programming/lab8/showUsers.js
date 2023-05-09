$((function () {

    // customize the dimensions of the input fields for filtering
    document.getElementById("role").style.height="40px";
    document.getElementById("role").style.width="400px";
    document.getElementById("name").style.height="40px";
    document.getElementById("name").style.width="400px";

    // function used to refresh a table of users displayed on a web page
    function refresh() {
        let role = $("#role")  // select input element for 'role'
        let name = $("#name")  // select input element for 'name'

        // the getJSON() method is used to get JSON data using an AJAX HTTP GET request
        // for each user returned in the JSON response, the function appends a new table row with the user's details
        $.getJSON("showUsers.php", {role: role.val(), name: name.val()}, function (json) {
            $("table tr:gt(0)").remove()
            json.forEach(function (thing) {
                $("table").append(`<tr>
                                <td>${thing[1]}</td>
                                <td>${thing[2]}</td>
                                <td>${thing[3]}</td>
                                <td>${thing[4]}</td>
                                <td>${thing[5]}</td>
                                <td>${thing[6]}</td>
                                <td>
                                    <a href=updateUser.php?id=${thing[0]}>Update</a>  <!--  link to update the user  -->
                                    <br>
                                    <a href=deleteUser.php?id=${thing[0]}>Delete</a>  <!--  link to delete the user  -->
                                    <br>
                                </td>
                               </tr>`)
            })
        })
    }

    // event listener to the input fields for filtering
    // when the user inputs a value to either of these field, the refresh() function is automatically called
    $("#role, #name").on("input", function () {
        refresh()
    })

    refresh()
}));


// function to check is a field is numeric
function isNumeric(n) {
    if (typeof n != "string") {
        return false;
    } else {
        return !isNaN(n) && !isNaN(parseFloat(n));
    }
}


// the parameter is the number of the column which the sorting is done on
function sortTable(n) {
    let table, rows, switching, i, x, y, shouldSwitch, direction, switchCount = 0;
    table = document.getElementById("usersTable");  // use a variable for the user table
    switching = true;
    direction = "asc";

    while (switching) {
        switching = false;
        // the rows of the table are stored here
        rows = table.rows;

        // loop through all the rows
        for (i = 1; i < (rows.length - 1); i++) {

            // this variable is set to true if the values in x and y need to be swapped
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];      // current row
            y = rows[i + 1].getElementsByTagName("td")[n];  // next row

            // sort the elements ascending
            if (direction === "asc") {
                if (!isNumeric(x.innerHTML) && !isNumeric(y.innerHTML)) {
                    if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                } else {
                    if (Number(x.innerHTML) > Number(y.innerHTML)) {
                        shouldSwitch = true;
                        break;
                    }
                }
                // sort the elements descending
            } else if (direction === "desc") {
                if (!isNumeric(x.innerHTML) && !isNumeric(y.innerHTML)) {
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                } else {
                    if (Number(x.innerHTML) < Number(y.innerHTML)) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
        }

        // if shouldSwitch is true, then the rows are swapped
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchCount++;
        } else {
            // if switchCount is zero and the current direction is ascending, the direction is changed to descending
            // and the switching variable is set to true.
            if (switchCount === 0 && direction === "asc") {
                direction = "desc";
                switching = true;
            }
        }
    }

    // idUp and idDown represent the IDs of the up and down arrows used to indicate the sorting direction.
    let idUp = "column" + (n + 1) + "-up";
    let idDown = "column" + (n + 1) + "-down";
    let idDown2;
    let idUp2;

    // if the current column is not the same as the last sorted column, the up and down arrow visibility
    // for the last sorted column is set to hidden
    if (n + 1 !== i) {
        idUp2 = "column" + (i) + "-up";
        idDown2 = "column" + (i) + "-down";
        document.getElementById(idUp2).style.visibility = "hidden";
        document.getElementById(idDown2).style.visibility = "hidden";
    }

    // mark the idUp and idDown as visible/hidden based on the sorting direction
    if (direction === "asc") {
        document.getElementById(idUp).style.visibility = "visible";
        document.getElementById(idDown).style.visibility = "hidden";
    } else {
        document.getElementById(idUp).style.visibility = "hidden";
        document.getElementById(idDown).style.visibility = "visible";
    }
}