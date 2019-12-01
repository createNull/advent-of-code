const fs = require('fs')

function get_fuel(mass) {
    return parseInt(mass / 3) - 2
}

function get_additional_fuel(fuel) {
    let total = 0
    while (fuel) {
        fuel = get_fuel(fuel)
        if (fuel < 0) break;
        total += fuel
    }
    return total
}

fs.readFile('input.txt', 'utf-8', function (err, file) {
    if (err) throw err;

    let total = 0
    let func_name = 'get_fuel'
    lines = file.split('\n').filter(Boolean)
    for (let line of lines) {
        num = parseInt(line)
        if (process.argv[2] == '2') {
            func_name = 'get_additional_fuel'
        }
        fuel = eval(`${func_name}(num)`)
        total += fuel
    }
    console.log(total)
});