const regex = {
	user: /^[a-zA-Z0-9]{4,30}$/,
	mail: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
  pass: /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$/,
};

function checkUsername(valor){    
    if (valor == "") {
      return false;
      }
      else {
        return regex.user.test(valor);
      } 
};

function checkCorreo(valor){  
    if (valor == "") {
      return false;
      }
      else {
        return regex.mail.test(valor);
      }
};

function checkContrasena(valor){
      if (valor == "") {
      return false;
      }
      else {
        return regex.pass.test(valor);
      }
};

function checkConfirmContrasena (valor1, valor2){
    if (valor2 == "") {
      return false;
      }
      else if(valor2 !== valor1) {
        return false; 
      }
      else {
        return regex.pass.test(valor2);
      }  
};

module.exports = {checkUsername, checkCorreo, checkContrasena, checkConfirmContrasena}


