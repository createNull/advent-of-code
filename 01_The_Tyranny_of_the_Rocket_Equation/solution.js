const fs = require('fs')

const array = fs.readFileSync('input.txt').toString().split(
    "\n").filter(Boolean).map(Number)

const calcTotalFuel = (input, option) =>
    input.reduce((total, moduleMass) => {
        const fuelNeeded = option == 2 ? massFuel(moduleMass) : requiredFuel(moduleMass)
        return total + fuelNeeded
    }, 0)

const requiredFuel = (mass) => Math.floor(mass / 3) - 2

const massFuel = (mass) => {
    const fuel = requiredFuel(mass)
    return fuel < 0 ? 0 : fuel + massFuel(fuel)
}

console.log('Part 1: ', calcTotalFuel(array))
console.log('Part 2: ', calcTotalFuel(array, 2))