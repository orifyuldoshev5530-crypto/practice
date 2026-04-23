/* C-TASK 

Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true; */

// Masalaning yechimi:

function checkContent(a, b) {
    return a.split('').sort().join() === b.split('').sort().join()
}
let result = checkContent("bahor", "roabh")
console.log("result:", result)

// ============================================================

/* B-TASK

Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin,
hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

// MASALANING yechimi:
function countDigits(str) {
    let count = 0;

    for (let i = 0; i < str.length; i++) {
        if (/\d/.test(str[i]))
            count++
    }
    return count;
}
console.log("result of count:", countDigits("ps35gv223fg")) */

// =====================================================================

/* A-TASK
Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi 
letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi. 

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
console.log("result:", countN("a", "panda")) */
