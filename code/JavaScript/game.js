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
            tile.src = "../../Pictures/Level1/blank.jpg";

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
        tile.src = "../../Pictures/Level1/"+pieces[i]+".jpg";
        document.getElementById("pieces").append(tile)
    }
}