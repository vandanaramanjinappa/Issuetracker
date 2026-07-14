// Load all issues when page opens
document.addEventListener("DOMContentLoaded", function () {
    loadIssues();
});


// GET - Display issues from database
function loadIssues() {

    let severityElement = document.getElementById("searchSeverity");
    let sortElement = document.getElementById("sortOrder");

    let severity = severityElement ? severityElement.value : "";
    let sort = sortElement ? sortElement.value : "asc";

    fetch(`/issues?severity=${severity}&sort=${sort}`)

        .then(response => response.json())

        .then(data => {

            let table = document.getElementById("issueTable");

            table.innerHTML = "";

            data.forEach(issue => {

                let row = `

                <tr>

                    <td>${issue.id}</td>

                    <td>${issue.title}</td>

                    <td>${issue.description}</td>

                    <td>${issue.severity}</td>

                    <td>${issue.status}</td>

                    <td>

                        <button onclick="editIssue(${issue.id})">
                        Edit
                        </button>

                        <button onclick="deleteIssue(${issue.id})">
                        Delete
                        </button>

                    </td>

                </tr>

                `;

                table.innerHTML += row;

            });

            updateDashboard(data);

        });

}



// POST - Create new issue

function createIssue() {

    let issue = {

        title: document.getElementById("title").value,

        description: document.getElementById("description").value,

        severity: document.getElementById("severity").value,

        status: document.getElementById("status").value

    };

    fetch("/issues", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(issue)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadIssues();

    });

}



// DELETE - Remove issue

function deleteIssue(id) {

    fetch(`/issues/${id}`, {

        method: "DELETE"

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadIssues();

    });

}
// PUT - Update existing issue

function editIssue(id) {

    let title = prompt("Enter new title:");

    let description = prompt("Enter new description:");

    let severity = prompt("Enter new severity (Critical, High, Medium, Low):");

    let status = prompt("Enter new status (Open, In Progress, Resolved):");

    if (title === null || description === null || severity === null || status === null) {
        return;
    }

    let updatedIssue = {

        title: title,

        description: description,

        severity: severity,

        status: status

    };

    fetch(`/issues/${id}`, {

        method: "PUT",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(updatedIssue)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadIssues();

    });

}


// Dashboard counts

function updateDashboard(data) {

    document.getElementById("totalIssues").innerHTML = data.length;

    document.getElementById("openIssues").innerHTML =
        data.filter(issue => issue.status === "Open").length;

    document.getElementById("progressIssues").innerHTML =
        data.filter(issue => issue.status === "In Progress").length;

    document.getElementById("resolvedIssues").innerHTML =
        data.filter(issue => issue.status === "Resolved").length;

} 