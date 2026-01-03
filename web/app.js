const boardState = [
  [ {f:'Y', b:'R'}, {f:'B', b:'R'}, {f:'R', b:'Y'}, {f:'B', b:'R'} ],
  [ {f:'Y', b:'R'}, null,           {f:'B', b:'R'}, {f:'B', b:'Y'} ],
  [ {f:'R', b:'B'}, {f:'B', b:'R'}, {f:'Y', b:'R'}, {f:'R', b:'B'} ],
  [ {f:'Y', b:'R'}, null,           {f:'R', b:'Y'}, {f:'B', b:'Y'} ],
];

const board = document.getElementById("board");

boardState.forEach(row => {
  row.forEach(cell => {
    const div = document.createElement("div");
    div.className = "cell";

    if (cell) {
      div.dataset.front = cell.f;
      div.dataset.back  = cell.b;
    }

    board.appendChild(div);
  });
});
