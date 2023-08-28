document.addEventListener("DOMContentLoaded", function () {
    const chessboard = document.getElementById("chessboard");
    const startAnimationBtn = document.getElementById("startAnimation");
    const timeGraph = document.getElementById("timeGraph");

    const inputs = [];
    const times = [];

    function createChessboard() {
        for (let i = 0; i < 64; i++) {
            const cell = document.createElement("div");
            cell.classList.add("cell");
            chessboard.appendChild(cell);
        }
    }

    createChessboard();

    const cells = document.querySelectorAll(".cell");

    // Function to animate the 8 Queens using Backtracking
    function animateQueens() {
        // Add your animation logic here
    }

    // Function to plot the graph using Chart.js
    function plotGraph() {
        const ctx = timeGraph.getContext("2d");

        new Chart(ctx, {
            type: "line",
            data: {
                labels: inputs.map(input => input.toString()),
                datasets: [{
                    label: "Time Taken",
                    data: times,
                    backgroundColor: "rgba(106, 176, 76, 0.2)",
                    borderColor: "rgba(106, 176, 76, 1)",
                    borderWidth: 2,
                    pointRadius: 4,
                    pointBackgroundColor: "rgba(106, 176, 76, 1)",
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: "Input Size"
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: "Time Taken (ms)"
                        }
                    }
                }
            }
        });
    }

    startAnimationBtn.addEventListener("click", function () {
        // ... animation logic

        // Simulate time taken for animation
        const simulatedTimeTaken = Math.random() * 1000; // Replace with actual time measurement

        // Add inputs and corresponding times for the graph
        inputs.push(inputs.length + 1); // Simulated input size
        times.push(simulatedTimeTaken);

        plotGraph();
    });
});
