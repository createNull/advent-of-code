const fs = require('fs')

const array = fs.readFileSync('input.txt').toString().split(
    "\n").filter(Boolean).map(Number)

function calculateTotalFuelNeeded(input) {
    return input.reduce((total, moduleMass) => {
        const funcName = process.argv[2] === '2' ? 'getFuelForMass' : 'getFuel'
        const fuelNeeded = eval(`${funcName}(moduleMass)`)
        return total + fuelNeeded
    }, 0)
}

function getFuel(mass) {
    return parseInt(mass / 3) - 2
}

function getFuelForMass(mass) {
    const fuel = getFuel(mass)
    return fuel < 0 ? 0 : fuel + getFuelForMass(fuel)
}

console.log(calculateTotalFuelNeeded(array))