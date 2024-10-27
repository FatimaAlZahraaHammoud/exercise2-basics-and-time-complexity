var x = parseInt(prompt("Enter a number"));

for (var i = 0; i <= x; i++){
    var num = 1;
    var line = ""
    for(var j = 0; j <= i; j++){
        line += num.toString() + " ";
        num += 2;
    }
    console.log(line);
}