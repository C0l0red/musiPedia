import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faEnvelope, faKey } from '@fortawesome/free-solid-svg-icons'
import '../auth.css';

export default class Register extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            username: "",
            email: "",
            password: "",
            confirmPassword: ""
        }
    }
    
    handleSubmit = event => {
        event.preventDefault();
        console.log("form submitted")
        console.log(this.state)
    }

    render() {
        return (
            <div className="d-flex justify-content-center h-100">
                <div className="card">
                    <div className="card-header">
                        <h3>Register</h3>
                    </div>
                    <div className="card-body">
                        <form onSubmit={this.handleSubmit}>
                            <div className="input-group form-group mb-3">
                                {/* <label>First Name</label> */}
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
                                {/* <label>Email</label> */}
                                <div className="input-group-prepend">
                                    <span className="input-group-text h-100">
                                        <FontAwesomeIcon icon={faEnvelope} />
                                    </span>
                                </div>
                                <input className="form-control" type="email" placeholder="email" 
                                    onChange={event => this.setState({email: event.target.value})} 
                                />
                            </div>
                            <div className="input-group form-group mb-3">
                                {/* <label>Password</label> */}
                                <div className="input-group-prepend">
                                    <span className="input-group-text h-100">
                                        <FontAwesomeIcon icon={faKey} />
                                    </span>
                                </div>
                                <input className="form-control" type="password" placeholder="password" 
                                    onChange={event => this.setState({password: event.target.value})} 
                                />
                            </div>
                            <div className="input-group form-group mb-3">
                                {/* <label>Confirm Password</label> */}
                                <div className="input-group-prepend">
                                    <span className="input-group-text h-100">
                                        <FontAwesomeIcon icon={faKey} />
                                    </span>
                                </div>
                                <input className="form-control" type="password" placeholder="confirm password" 
                                    onChange={event => this.setState({confirmPassword: event.target.value})} 
                                />
                            </div>
                            <div className="form-grouo">
                                <button type="submit" className="btn btn-primary submit-btn">Register</button>
                            </div>
                        </form>
                    </div>
                    <div className="card-footer">
                        <div className="d-flex justify-content-center links">
                            Already have an account?<a href="">Sign In</a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
