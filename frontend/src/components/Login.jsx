import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faKey } from '@fortawesome/free-solid-svg-icons'
import '../auth.css';
import axios from 'axios';

export default class Login extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            username: "",
            password: ""
        }
    }
    
    handleSubmit = event => {
        event.preventDefault();
        console.log(this.state)
        let data = {username: this.state.email, 
                    password: this.state.password};
        let config = {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
        axios.post("/auth/token/login", data, config)
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.log(err)
            })
    }

    render() {
        return (
            <div className="d-flex justify-content-center h-100">
                <div className="card">
                    <div className="card-header">
                        <h3>Login</h3>
                    </div>
                    <div className="card-body">
                        <form onSubmit={this.handleSubmit}>
                            <div className="input-group form-group mb-3">
                                <div className="input-group-prepend">
                                    <span className="input-group-text h-100">
                                        <FontAwesomeIcon icon={faUser} />
                                    </span>
                                </div>
                                <input className="form-control" type="text" placeholder="username"
                                    onChange={event => this.setState({username: event.target.value})} 
                                />
                            </div>
                            <div className="input-group form-group mb-3">
                                <div className="input-group-prepend">
                                    <span className="input-group-text h-100">
                                        <FontAwesomeIcon icon={faKey} />
                                    </span>
                                </div>
                                <input className="form-control" type="password" id="password" placeholder="password"
                                    onChange={event => this.setState({password: event.target.value})} 
                                />
                            </div>
                            <div className="row align-items-center remember mb-3">
						        <input type="checkbox"/>Remember Me
					        </div>
                            <div className="form-group justify-content-end">
                                <button type="submit" className="btn btn-primary submit-btn">Login</button>
                            </div>
                        </form>
                    </div>
                    <div className="card-footer">
                        <div className="d-flex justify-content-center links">
                            Don't have an account?<a href="">Sign Up</a>
                        </div>
                        <div className="d-flex justify-content-center">
                            <a href="">Forgot your password?</a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
