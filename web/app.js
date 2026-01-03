const SIZE = 4;
let turn = 0;

// 간단한 말 세트 (무한히 생성, 지금은 데모용)
const pieceCycle = [
  { f: "Y", b: "R" },
  { f: "B", b: "Y" },
  { f: "R", b: "B" },
];

let board = Array.from({ length: SIZE }, () =>
  Array(SIZE).fill(null)
);

const boardDiv = document.getElementById("board");
const turnText = document.getElementById("turn");

function render() {
  boardDiv.innerHTML = "";
  turnText.textContent = `턴 ${turn + 1}`;

  board.flat().forEach((cell, idx) => {
    const div = document.createElement("div");
    div.className = "cell";

    if (cell) {
      div.classList.add(`front-${cell.f}`);
      div.classList.add(`back-${cell.b}`);
    }

    div.onclick = () => onClickCell(Math.floor(idx / SIZE), idx % SIZE);
    boardDiv.appendChild(div);
  });
}

function onClickCell(x, y) {
  const cell = board[x][y];

  // 빈칸 → 착수
  if (!cell) {
    const p = pieceCycle[turn % 3];
    board[x][y] = { ...p, front: true };
    turn++;
  }
  // 말 있음 → 뒤집기
  else {
    [cell.f, cell.b] = [cell.b, cell.f];
    turn++;
  }

  if (checkBingo()) {
    alert("빙고!");
  }

  render();
}

function checkBingo() {
  const lines = [];

  for (let i = 0; i < SIZE; i++) {
    lines.push([...Array(SIZE)].map((_, j) => [i, j]));
    lines.push([...Array(SIZE)].map((_, j) => [j, i]));
  }

  lines.push([...Array(SIZE)].map((_, i) => [i, i]));
  lines.push([...Array(SIZE)].map((_, i) => [i, SIZE - 1 - i]));

  return lines.some(line => {
    const first = board[line[0][0]][line[0][1]];
    if (!first) return false;
    return line.every(([x, y]) =>
      board[x][y] && board[x][y].f === first.f
    );
  });
}

render();
