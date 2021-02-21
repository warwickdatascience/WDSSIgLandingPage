import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Foot from './Footer';
import Overlay from './Overlay';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
ReactDOM.render(<Foot />, document.getElementById('foot'));
ReactDOM.render(<Overlay />, document.getElementById('clicking'));
// registerServiceWorker();
