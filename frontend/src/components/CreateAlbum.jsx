import React, { Component } from 'react'

export default class CreateAlbum extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            title: "",
            artist: "",
            releaseDate: "",
            cover: "",
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
                        <label>Title</label>
                        <input className="form-control" type="text" id="title" 
                               onChange={event => this.setState({title: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Artist</label>
                        <input className="form-control" type="text" id="artist" 
                               onChange={event => this.setState({artist: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Release Date</label>
                        <input className="form-control" type="date" id="release-date" 
                               onChange={event => this.setState({releaseDate: event.target.value})} 
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
                        <label>Cover</label>
                        <input className="form-control" type="image" id="cover" 
                               onChange={event => this.setState({cover: event.target.value})} 
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
