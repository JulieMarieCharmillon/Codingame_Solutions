function Counter(array) {
    let finale = []
    for (var i=0; i<array.length; i++) {
        if (array[i] !== "'") {
            if (array[i].endsWith("'")===true) {
              finale.push(array[i].replace("'",""))
            }
            else {finale.push(array[i])}
        }
    }
    return finale.forEach(val => this[val] = (this[val] || 0) + 1);
}

export const countWords = (sentence) => {
  let regex = sentence.toLowerCase().replace(/[^a-z0-9\']/g, " ").replace(/\b' /g," ").replace(/ '\b/g," ").replace(/\s+/gi, " ").trim();
  let liste = regex.split(" ");
  console.log(new Counter(liste));
  return new Counter(liste)
};
