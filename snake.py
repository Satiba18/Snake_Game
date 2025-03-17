import streamlit as st

st.title("Snake Game 🐍")
st.markdown("**Click the game area first**, then use arrow keys → ↑ ← ↓")

snake_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        #gameCanvas {
            background: #2c3e50;
            display: block;
            margin: 0 auto;import streamlit as st

st.title("Snake Game ")
st.markdown("**Click the game area first**, then use arrow keys → ↑ ← ↓")

snake_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        #gameCanvas {
            background: #2c3e50;
            display: block;
            margin: 0 auto;
            border-radius: 10px;
            cursor: pointer;
        }
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400" tabindex="0"></canvas>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const gridSize = 20;
        const tileCount = 20;
        
        let snake = [{x: 10, y: 10}];
        let food = {x: 15, y: 15};
        let dx = 1;
        let dy = 0;
        let score = 0;
        let lastUpdate = 0;
        const gameSpeed = 150;

        // Focus canvas automatically
        canvas.focus();
        
        function gameLoop(timestamp) {
            if (timestamp - lastUpdate > gameSpeed) {
                const head = {
                    x: (snake[0].x + dx + tileCount) % tileCount,
                    y: (snake[0].y + dy + tileCount) % tileCount
                };

                if (snake.some(segment => segment.x === head.x && segment.y === head.y)) {
                    resetGame();
                }

                snake.unshift(head);
                if (head.x === food.x && head.y === food.y) {
                    score += 10;
                    spawnFood();
                } else {
                    snake.pop();
                }
                lastUpdate = timestamp;
            }

            // Drawing
            ctx.fillStyle = '#2c3e50';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw snake
            ctx.fillStyle = '#2ecc71';
            snake.forEach(segment => {
                ctx.beginPath();
                ctx.arc(
                    segment.x * gridSize + gridSize/2,
                    segment.y * gridSize + gridSize/2,
                    gridSize/2 - 1,
                    0,
                    Math.PI * 2
                );
                ctx.fill();
            });

            // Draw food
            ctx.fillStyle = '#e74c3c';
            ctx.beginPath();
            ctx.arc(
                food.x * gridSize + gridSize/2,
                food.y * gridSize + gridSize/2,
                gridSize/2 - 1,
                0,
                Math.PI * 2
            );
            ctx.fill();

            // Score
            ctx.fillStyle = 'white';
            ctx.font = '20px Arial';
            ctx.fillText(`Score: ${score}`, 10, 30);

            requestAnimationFrame(gameLoop);
        }

        function spawnFood() {
            do {
                food = {
                    x: Math.floor(Math.random() * tileCount),
                    y: Math.floor(Math.random() * tileCount)
                };
            } while(snake.some(segment => segment.x === food.x && segment.y === food.y));
        }

        function resetGame() {
            snake = [{x: 10, y: 10}];
            dx = 1;
            dy = 0;
            score = 0;
            spawnFood();
        }

        // Key handler with event prevention
        canvas.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'ArrowUp': 
                    if (dy === 0) { dx = 0; dy = -1; e.preventDefault(); }
                    break;
                case 'ArrowDown':
                    if (dy === 0) { dx = 0; dy = 1; e.preventDefault(); }
                    break;
                case 'ArrowLeft':
                    if (dx === 0) { dx = -1; dy = 0; e.preventDefault(); }
                    break;
                case 'ArrowRight':
                    if (dx === 0) { dx = 1; dy = 0; e.preventDefault(); }
                    break;
            }
        });

        // Click to focus
        canvas.addEventListener('click', () => {
            canvas.focus();
        });

        // Start game
        spawnFood();
        requestAnimationFrame(gameLoop);
    </script>
</body>
</html>
"""

st.components.v1.html(snake_html, height=420)
            border-radius: 10px;
            cursor: pointer;
        }
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400" tabindex="0"></canvas>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const gridSize = 20;
        const tileCount = 20;
        
        let snake = [{x: 10, y: 10}];
        let food = {x: 15, y: 15};
        let dx = 1;
        let dy = 0;
        let score = 0;
        let lastUpdate = 0;
        const gameSpeed = 150;

        // Focus canvas automatically
        canvas.focus();
        
        function gameLoop(timestamp) {
            if (timestamp - lastUpdate > gameSpeed) {
                const head = {
                    x: (snake[0].x + dx + tileCount) % tileCount,
                    y: (snake[0].y + dy + tileCount) % tileCount
                };

                if (snake.some(segment => segment.x === head.x && segment.y === head.y)) {
                    resetGame();
                }

                snake.unshift(head);
                if (head.x === food.x && head.y === food.y) {
                    score += 10;
                    spawnFood();
                } else {
                    snake.pop();
                }
                lastUpdate = timestamp;
            }

            // Drawing
            ctx.fillStyle = '#2c3e50';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw snake
            ctx.fillStyle = '#2ecc71';
            snake.forEach(segment => {
                ctx.beginPath();
                ctx.arc(
                    segment.x * gridSize + gridSize/2,
                    segment.y * gridSize + gridSize/2,
                    gridSize/2 - 1,
                    0,
                    Math.PI * 2
                );
                ctx.fill();
            });

            // Draw food
            ctx.fillStyle = '#e74c3c';
            ctx.beginPath();
            ctx.arc(
                food.x * gridSize + gridSize/2,
                food.y * gridSize + gridSize/2,
                gridSize/2 - 1,
                0,
                Math.PI * 2
            );
            ctx.fill();

            // Score
            ctx.fillStyle = 'white';
            ctx.font = '20px Arial';
            ctx.fillText(`Score: ${score}`, 10, 30);

            requestAnimationFrame(gameLoop);
        }

        function spawnFood() {
            do {
                food = {
                    x: Math.floor(Math.random() * tileCount),
                    y: Math.floor(Math.random() * tileCount)
                };
            } while(snake.some(segment => segment.x === food.x && segment.y === food.y));
        }

        function resetGame() {
            snake = [{x: 10, y: 10}];
            dx = 1;
            dy = 0;
            score = 0;
            spawnFood();
        }

        // Key handler with event prevention
        canvas.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'ArrowUp': 
                    if (dy === 0) { dx = 0; dy = -1; e.preventDefault(); }
                    break;
                case 'ArrowDown':
                    if (dy === 0) { dx = 0; dy = 1; e.preventDefault(); }
                    break;
                case 'ArrowLeft':
                    if (dx === 0) { dx = -1; dy = 0; e.preventDefault(); }
                    break;
                case 'ArrowRight':
                    if (dx === 0) { dx = 1; dy = 0; e.preventDefault(); }
                    break;
            }
        });

        // Click to focus
        canvas.addEventListener('click', () => {
            canvas.focus();
            e.preventDefault();
        });

        // Start game
        spawnFood();
        requestAnimationFrame(gameLoop);
    </script>
</body>
</html>
"""

st.components.v1.html(snake_html, height=420)