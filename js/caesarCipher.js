exports.caesarCipher = function(str, num) {
    let copy = str.toUpperCase()
    let indexes = []
    let shifter = []
    let numCounter = 0
    let upper = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
    for(let i = 0; i < copy.length; i++){
      let same = (element) => element == copy[i];
      if(upper.findIndex(same) == -1){
        indexes.push(copy[i])
      } else
      indexes.push(upper.findIndex(same))
    }
  
    if(num > 0){
        while(numCounter != num){
          upper.push(upper.shift())
          numCounter++
        }
      }else{
        while(numCounter != num){
          upper.unshift(upper.pop())
          numCounter--
        }
      }
  
    for(let i = 0; i < indexes.length; i++){
      if(upper[indexes[i]] == undefined || typeof indexes[i] == 'string'){
        shifter.push(indexes[i])
      } else if (str[i] == str[i].toLowerCase()){
    shifter.push(upper[indexes[i]].toString().toLowerCase())
      } else
      shifter.push(upper[indexes[i]])
    }

    return shifter.join(''); 
};
