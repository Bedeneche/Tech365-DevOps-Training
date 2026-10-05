const express = require("express");

const app = express();
const PORT = 3000;

// Allow the API to receive JSON data
app.use(express.json());

// Simple employee data
let employees = [
    {
        id: 1,
        name: "neche ",
        position: "IT Support"
    },
    {
        id: 2,
        name: "bede chukwude",
        position: "DevOps Engineer"
    },
    {
        id: 3,
        name: "chukwuma",
        position: "Software Engineer"
    },
    {
        id: 4,
        name: "maria Ani",
        position: "Product Manager"
    },
    {
        id: 5,
        name: "john ude",
        position: "UX Designer"
    },
    {
        id: 6,
        name: "Wale jumoke",
        position: "chief technology officer"
    }
];

// Home route
app.get("/", (req, res) => {
    res.send("Employee API is running");
});

// Get all employees
app.get("/employees", (req, res) => {
    res.json(employees);
});

// Get one employee
app.get("/employees/:id", (req, res) => {
    const id = Number(req.params.id);

    const employee = employees.find(employee => employee.id === id);

    if (!employee) {
        return res.status(404).json({
            message: "Employee not found"
        });
    }

    res.json(employee);
});

// Add a new employee
app.post("/employees", (req, res) => {
    const newEmployee = {
        id: employees.length + 1,
        name: req.body.name,
        position: req.body.position
    };

    employees.push(newEmployee);

    res.status(201).json(newEmployee);
});

// Delete an employee
app.delete("/employees/:id", (req, res) => {
    const id = Number(req.params.id);

    employees = employees.filter(employee => employee.id !== id);

    res.json({
        message: "Employee deleted"
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Employee API running on port ${PORT}`);
});
