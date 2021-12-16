const username = document.getElementById('username');
const email = document.getElementById('correo');
const password = document.getElementById('contrasena');
const password2 = document.getElementById('confirmar_contrasena');
const form = document.getElementById('form-registro');

const regex = {
	user: /^[a-zA-Z0-9]{6,30}$/,
	mail: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
  pass: /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$/,
};

function checkUsername(valor){
    let valid = false;
    
    if (valor === "" || valor === null) {
        document.getElementById('error_user').innerHTML="*Campo obligatorio.";
        showError(username);
      }
      else if (!(regex.user.test(valor))) {
        document.getElementById('error_user').innerHTML="*El nombre de usuario debe tener entre 4 y 30 caracteres. No incluya caracteres especiales.";
        showError(username);  
      } 
      else {
        showSuccess(username);
        valid = true;
      }
    
    return valid;
}

function checkCorreo(valor){  
    let valid = false;
    
    if (valor === "" || valor === null) {
        document.getElementById('error_email').innerHTML="*Campo obligatorio.";
        showError(email, "Campo obligatorio");
      }
      else if (!(regex.mail.test(valor))) {
        document.getElementById('error_email').innerHTML="*Verifique que su correo electrónico tenga el formato: usuario@correo.com";
        showError(email);  
      } 
      else {
        showSuccess(email);
        valid = true;
      }
    return valid;
}

function checkContrasena(valor){
    let valid = false;
    if (valor === "" || valor === null) {
        document.getElementById('error_pass').innerHTML="*Campo obligatorio.";
        showError(password);
      }
      else if (!(regex.pass.test(valor))) {
        document.getElementById('error_pass').innerHTML="*La contraseña debe tener al menos una letra mayúscula, una letra minúscula, un número y una longitud mínima de 8 caracteres.";
        showError(password);  
      } 
      else {
        showSuccess(password);
        valid = true;
      }  
    return valid;
}

function checkConfirmContrasena (valor1, valor2){
    let valid = false;
    if (valor2 === "" || valor2 === null) {
        document.getElementById('error_pass2').innerHTML="*Campo obligatorio.";
        showError(password2);
      }
      else if(valor2 !== valor1) {
        document.getElementById('error_pass2').innerHTML="*La contraseña no coincide con la ingresada previamente.";
        showError(password2); 
      }
      else {
        showSuccess(password2);
        valid = true;
      }  
    return valid;
}

function showError (input) {
    const formField = input.parentElement;
    formField.className = 'form-field error';                                               
  }

function showSuccess (input) {
    const formField = input.parentElement;
    formField.className = 'form-field success';
  }

  form.addEventListener('submit', function (e) {      
    e.preventDefault();

    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();

    let isUsernameValid = checkUsername(usernameValue),
        isEmailValid = checkCorreo(emailValue),
        isPasswordValid = checkContrasena(passwordValue),
        isConfirmPasswordValid = checkConfirmContrasena(passwordValue,password2Value);

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isPasswordValid &&
        isConfirmPasswordValid;

    if (isFormValid) {
        alert("Registro exitoso");
    }
});