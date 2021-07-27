import React, { Component } from 'react'

export default class CreateArtist extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            realName: "",
            stageName: "",
            recordLabel: "",
            dateOfBirth: "",
            dateOfDeath: "",
            picture: "",
            rating: ""
        }
    }
    
    handleSubmit = event => {
        event.preventDefault();
        console.log(this.state)
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <div className="form-group">
                        <label>Real Name</label>
                        <input className="form-control" type="text" id="real-name" 
                               onChange={event => this.setState({realName: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Stage Name</label>
                        <input className="form-control" type="text" id="stage-name" 
                               onChange={event => this.setState({stageName: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Record Label</label>
                        <input className="form-control" type="text" id="record-label" 
                               onChange={event => this.setState({recordLabel: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Date Of Birth</label>
                        <input className="form-control" type="date" id="date-of-birth" 
                               onChange={event => this.setState({dateOfBirth: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Date Of Death</label>
                        <input className="form-control" type="date" id="date-of-death" 
                               onChange={event => this.setState({dateOfDeath: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Picture</label>
                        <input className="form-control" type="image" id="picture" 
                               onChange={event => this.setState({picture: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Rating</label>
                        <input className="form-control" type="number" id="rating" 
                               onChange={event => this.setState({rating: event.target.value})} 
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Login</button>
                </form>
            </div>
        )
    }
}
