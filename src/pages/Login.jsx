import React from 'react';
import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn } from 'mdbreact';

import './styles/Login.scss';

const Login = () => (
  <div id="login-wrapper">
    <MDBContainer id="login" className="card p-5">
      <MDBRow>
        <MDBCol>
          <form>
            <p className="h5 text-center mb-4 font-weight-bold">INICIAR SESIÓN</p>
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
      </MDBRow>
    </MDBContainer>
  </div>
);

export default Login;