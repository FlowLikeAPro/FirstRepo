let currentPlayer = 'X';
let board = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

function makeMove(cell) {
    if (gameActive && board[cell] === '') {
        board[cell] = currentPlayer;
        document.getElementsByClassName('cell')[cell].innerText = currentPlayer;
        checkWinner();
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';

        document.getElementById('currentPlayer').innerText = `Current Player: ${currentPlayer}`;
    }
}

function checkWinner() {
    const winPatterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];

    for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (board[a] && board[a] === board[b] && board[b] === board[c]) {
            gameActive = false;
            document.getElementById('result').innerText = `${board[a]} wins!`;
        }
    }

    if (!board.includes('') && gameActive) {
        gameActive = false;
        document.getElementById('result').innerText = "It's a draw!";
    }
}

function resetBoard() {
    currentPlayer = 'X';
    board = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    document.getElementById('result').innerText = '';
    for (let cell of document.getElementsByClassName('cell')) {
        cell.innerText = '';
    }
}

resetBoard();
