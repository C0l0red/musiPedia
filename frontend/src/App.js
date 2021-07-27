import logo from './logo.svg';
import './App.css';
import {Link, Route, Switch} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Homepage from './components/Homepage';
import Login from './components/Login';
import Register from './components/Register';
import Artists from './components/Artists';
import Albums from './components/Albums';
import Songs from './components/Songs';
import CreateArtist from './components/CreateArtist';
import CreateAlbum from './components/CreateAlbum';
import CreateSong from './components/CreateSong';

function App() {
  return (
    <div className="App container">
      <Switch>
        <Route exact path="/" component={Homepage}/>
        <Route exact path="/login" component={Login}/>
        <Route exact path="/register" component={Register}/>
        <Route path="/artists" component={Artists}/>
        <Route path="/albums" component={Albums}/>
        <Route path="/songs" component={Songs}/>
        <Route path="/create-artist" component={CreateArtist}/>
        <Route path="/create-album" component={CreateAlbum}/>
        <Route path="/create-song" component={CreateSong}/>
      </Switch>
    </div>
  );
}

export default App;
