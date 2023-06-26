/* CONDICIONES LOGIN */
const login = document.getElementById('login');
const inputs = document.querySelectorAll('#login input');

const expresiones = {
    password: /^[a-zA-ZÁ0-9.]{8,12}$/,
    correo: /^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/   
}

const campos = {
    correo: false,
    password: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
        break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            validarPassword2();
        break;
        case "password2":
            validarPassword2();
        break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if(expresion.test(input.value)) {
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        /*document.querySelector('#grupo__correo i').classList.add('fa-solid fa-circle-check');
        document.querySelector('#grupo__correo i').classList.remove('fa-solid fa-circle-xmark');*/
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        /*document.querySelector('#grupo__correo i').classList.add('fa-solid fa-circle-xmark');
        document.querySelector('#grupo__correo i').classList.remove('fa-solid fa-circle-check');*/
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('password');
    const inputPassword2 = document.getElementById('password2');

    if(inputPassword1.value !== inputPassword2.value){
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
        /*document.querySelector('#grupo__password i').classList.add('fa-solid fa-circle-xmark');
        document.querySelector('#grupo__password i').classList.remove('fa-solid fa-circle-check');*/
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['password'] = false;
    } else {
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
        /*document.querySelector('#grupo__password i').classList.add('fa-solid fa-circle-xmark');
        document.querySelector('#grupo__password i').classList.remove('fa-solid fa-circle-check');*/
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['password'] = true;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

login.addEventListener('submit', (e) => {
	e.preventDefault();

    if(campos.correo && campos.password){
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 4000);
        
        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
        
        login.reset();

    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
        }, 4000);
    }
});