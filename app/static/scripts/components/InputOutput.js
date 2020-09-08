import React from 'react'
import styled from 'styled-components';
const InputOutput = () => {
    return (
        <Wrapper>
            <div className="io-field">
                <p>Input Text</p>
                <textarea name="input-text" id="input-text" rows="10"></textarea>
            </div>
            <div className="io-field">
                <p>Output Text</p>
                <textarea name="input-text" id="input-text" rows="10"></textarea>
            </div>
        </Wrapper>
    )
}
const Wrapper = styled.div`
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    .io-field {
        margin-top: 1rem;
        textarea {
            width:100%;
        }
    }
`;
export default InputOutput
