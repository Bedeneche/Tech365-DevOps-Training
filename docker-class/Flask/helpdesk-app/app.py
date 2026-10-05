from flask import Flask, render_template, request

app = Flask(__name__)

tickets = []


@app.route("/")
def home():
    return render_template("index.html", tickets=tickets)


@app.route("/create-ticket", methods=["POST"])
def create_ticket():
    name = request.form["name"]
    issue = request.form["issue"]
    priority = request.form["priority"]

    ticket = {
        "id": len(tickets) + 1,
        "name": name,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    tickets.append(ticket)

    return render_template("index.html", tickets=tickets)


@app.route("/update-status/<int:ticket_id>", methods=["POST"])
def update_status(ticket_id):
    new_status = request.form["status"]

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = new_status

    return render_template("index.html", tickets=tickets)


@app.route("/delete-ticket/<int:ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):
    global tickets

    tickets = [
        ticket for ticket in tickets
        if ticket["id"] != ticket_id
    ]

    return render_template("index.html", tickets=tickets)


if __name__ == "__main__":
    app.run(debug=True)