import React from 'react';

const Login = () => {
    return (
        <div>
            <div>
                <h1> LOGIN </h1>
            </div>
            <div className='row'>
                <div className='col-1'> 
                    <label htmlFor="username" className="col-sm-2 col-form-label fw-bolder"> Username</label>
                </div>
                
                <div className='col-2'>
                    <input type="text" className="form-control" id="username"/>
                </div>
            </div>

            <div className='row'>
                <div className='col-1'>
                    <label htmlFor="password" className="col-sm-2 col-form-label fw-bolder"> Password</label>    
                </div>
                
                <div className='col-2'>
                    <input type="password" className="form-control" id="password"/>
                </div>
            </div>

            <div className='mt-3'>
                <button className="btn btn-primary rounded-pill">Login</button>
            </div>
        </div>
    );
}
export default Login;