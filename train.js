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