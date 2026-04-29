
/* F-TASK 

Savol: Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi*/

// Masalaning yechimi:

function finding(non) {
    let bob = [...new Set(non)]
    if (bob.length !== non.length) {
        return true
    } return false
}
console.log("result:", finding("hello"))


// ===========================================================

/* E-TASK (NodeJS)

Savol: Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"

// Masalaning yechimi:

function getReverse(a) {
    return a.split("").reverse().join("")
}
console.log("result:", getReverse("Hello world"))
*/

// ===========================================================

/* D-TASK

Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.

// Masalaning yechimi:

function getIndex(arr) {
    let max = arr[0];
    let index = 0;

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
            index = i;
        }
    }
    return index;
}

console.log(getIndex([23, 6, 32, 17, 61, 55])); */


// ============================================================

/* C-TASK

Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;

// Masalaning yechimi:

function checkContent(a, b) {
    return a.split('').sort().join() === b.split('').sort().join()
}
let result = checkContent("bahor", "roabh")
console.log("result:", result) */

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
