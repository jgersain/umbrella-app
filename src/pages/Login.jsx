import React from 'react';
import { Link } from 'react-router-dom';
import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn } from 'mdbreact';

import './styles/Login.scss';

const Login = () => (
  <div id="login-wrapper">
    <MDBContainer id="login" className="card p-5">
      <MDBRow>
        <MDBCol>
          <form>
            <p className="h4 text-center mb-4 font-weight-bold text-muted">INICIAR SESIÓN</p>
            <div className="grey-text">
              <MDBInput
                label="Correo Electrónico"
                icon="envelope"
                group
                type="email"
                validate
                error="wrong"
                success="right"
              />
              <MDBInput
                label="Constraseña"
                icon="lock"
                group
                type="password"
                validate
              />
            </div>
            <div className="text-center">
              <MDBBtn className="btn peach-gradient font-weight-bold">Iniciar Sesión</MDBBtn>
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
);

export default Login;