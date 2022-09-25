let rows = 6;
let cols = 6;

var currTile;
var otherTile;

window.onload = function()
{
    for (let r=0; r < rows; r++)
    {
        for (let c=0; c < cols; c++)
        {
            let tile = document.createElement("img");
            tile.src = "../static/game_pictures/Level1/blank.jpg";

            tile.addEventListener("dragstart", dragStart);
            tile.addEventListener("dragover", dragOver);
            tile.addEventListener("dragenter",dragEnter);
            tile.addEventListener("dragleave",dragLeave);
            tile.addEventListener("drop", dragDrop);
            tile.addEventListener("dragend", dragEnd);  

            document.getElementById("board").append(tile)
        }
    }

    let pieces = [];
    for (let i=1; i <= rows*cols; i++)
    {
        pieces.push("image_part_"+i.toString());
    }
    pieces.reverse();
    for(let i=0; i<pieces.length; i++)
    {
        let j = Math.floor(Math.random() * pieces.length);
        let tmp = pieces[i];
        pieces[i] = pieces[j]
        pieces[j] = tmp
    }

    for(let i = 0; i < pieces.length; i++)
    {
        let tile = document.createElement("img");
        tile.src = "../static/game_pictures/Level1/"+pieces[i]+".jpg";

        tile.addEventListener("dragstart", dragStart);
        tile.addEventListener("dragover", dragOver);
        tile.addEventListener("dragenter",dragEnter);
        tile.addEventListener("dragleave",dragLeave);
        tile.addEventListener("drop", dragDrop);
        tile.addEventListener("dragend", dragEnd);
        document.getElementById("pieces").append(tile)
    }
}

function dragStart()
{
    currTile = this;
}

function dragOver(e)
{
    e.preventDefault();
}

function dragEnter(e)
{
    e.preventDefault();
}

function dragLeave()
{

}

function dragDrop()
{
    otherTile = this;
}

function dragEnd()
{
    if (currTile.src.includes("blank"))
    {
        return;
    }

    let currImg = currTile.src;
    let otherImg = otherTile.src;
    currTile.src = otherImg;
    otherTile.src = currImg;

    checkCorrect()
}

function checkCorrect()
{
    board = document.querySelectorAll('#board > *')
    let i = 1;
    for(const element of board)
    {
        let source = element.src.toString();
        let num = source.substring(source.search('part_')+5,source.search('.jpg'))
        if(i != num)
        {
            return;
        }
        i++;
    }
    alert("Level Cleared")
}