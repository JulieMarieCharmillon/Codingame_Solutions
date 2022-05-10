export const score = (letter) => {
    var score_value = 0
    const word = letter.toUpperCase()
    
    function getKeyByValue(object, l) {
      return Object.keys(object).find(key => object[key].includes(l));
  }
    const dict = {
      1: ["A","E", "I", "O", "U", "L", "N", "R", "S", "T"],
      2: ["D", "G"],
      3: ["B", "C", "M", "P"],
      4: ["F", "H", "V", "W", "Y"],
      5: ["K"],
      8: ["J", "X"],
      10:["Q", "Z"]    
    }
    
    for (let i = 0; i < word.length; i++) {
      var l = word[i];
      score_value += parseInt(getKeyByValue(dict, l))
    }
    
    return score_value
  };
  