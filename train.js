// A-TASK
// Masalaning sharti: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
// MASALAN countLetter("e", "engineer") 3ni return qiladi.

// MASALANING yechimi:
function countN(letter, word) {
    let count = 0;

    for (let i = 0; i < word.length; i++) {
        if (word[i] === letter) {
            count++
        }
    }
    return count;
}
console.log("result:", countN("a", "panda"))

function count1(words) {
    let total = 0

    for (i = 0; i < words.length; i++) {
        if (words[i] == "number") {
            total++
        }
    }
    return total
}

result1 = count1("sdf234b54")
console.log(result1)