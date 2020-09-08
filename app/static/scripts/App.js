import React, { Component } from 'react'
import Header from './components/Header';
import InputOutput from './components/InputOutput';
import CipherSelector from './components/CipherSelector';
import styled from 'styled-components';
class App extends Component {
    render() {
        return (
            <Wrapper>
                <div className="container mt-4 my-4 main-container">
                    <Header />
                    <CipherSelector />
                    <InputOutput />
                </div>
                
            </Wrapper>
        )
    }
}

const Wrapper = styled.div`
    .main-container {
        background-color: #e3fff3;
        border: 1px solid #98d9bd;
        border-radius: 5px;
    }
    
`;

export default App