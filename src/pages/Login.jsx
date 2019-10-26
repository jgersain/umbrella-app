import React, { useState }  from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { MDBContainer, MDBRow, MDBCol, MDBInput } from 'mdbreact';

import './styles/Login.scss';
import { loginRequest } from '../actions'

const Login = props => {
  const [form, setValues] = useState({
    email: '',
  })

  const handleInput = event => {
    setValues({
      ...form,
      [event.target.name]: event.target.value
    })
  }

  const handleSubmit = event => {
    event.preventDefault();
    props.loginRequest(form)
    props.history.push('/looking');
  }

  return (
    <div id="login-wrapper">
      <MDBContainer id="login" className="card p-5">
        <MDBRow>
          <MDBCol>
            <form onSubmit={handleSubmit}>
              <p className="h4 text-center mb-4 font-weight-bold text-muted">INICIAR SESIÓN</p>
              <div className="grey-text">
                <MDBInput
                  name="email"
                  label="Correo Electrónico"
                  icon="envelope"
                  group
                  type="email"
                  validate
                  error="wrong"
                  success="right"
                  onChange={handleInput}
                />
                <MDBInput
                  name="password"
                  label="Constraseña"
                  icon="lock"
                  group
                  type="password"
                  validate
                  onChange={handleInput}
                />
              </div>
              <div className="text-center">
                <button 
                  type="submit" 
                  className="btn peach-gradient font-weight-bold"
                >Iniciar Sesión
                </button>
              </div>
            </form>
          </MDBCol>
          <MDBCol md='12' className="pt-4">
            <p className='font-small d-flex justify-content-end'>
              ¿No tienes una cuenta?
              <Link to='/sign_up' className='text-default ml-1 font-weight-bold'>
                Registrate aquí! 
              </Link>
            </p>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </div>  
  )
}

// send data to actions 
const mapDispatchToProps = {
  loginRequest, 
}

export default connect(null, mapDispatchToProps)(Login);