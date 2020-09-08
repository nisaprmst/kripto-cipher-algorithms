import React, { useState } from 'react'
import styled from 'styled-components';
const CipherSelector = ({setCipherData, handleSubmit}) => {
    const [cipher, setCipher] = useState('vigenere');
    const [textData, setTextData] = useState('');

    const handleCipherSelected = (selectEl) => {
        const val = selectEl.options[selectEl.selectedIndex].value;
        setCipher(val);
    };

    const handleCipherSubmit = () => {
        const objToSubmit = {
            type: cipher,
            keys: []
        }
        if (cipher === 'vigenere') {
            objToSubmit.variant = document.querySelector('input[name="v_type"]:checked').value;
            objToSubmit.keys.push(document.getElementById('v_key').value);
        } else if (cipher === 'playfair') {
            objToSubmit.keys.push(document.getElementById('p_key').value);
        } else if (cipher === 'affine') {
            objToSubmit.keys.push(document.getElementById('a_key_a').value);
            objToSubmit.keys.push(document.getElementById('a_key_b').value);
        } else if (cipher === 'hill') {
            objToSubmit.keys.push(document.getElementById('h_key').value);
        } else if (cipher === 'supercipher') {

        } else { return; }
        objToSubmit.text = textData;
        setCipherData(objToSubmit);
        console.log(objToSubmit);
    }
    return (
        <Wrapper>
            <p>Cipher Method</p>
            <select name="cipher-selection" id="cipher-selection" onChange={(e) => handleCipherSelected(e.target)}>
                <option value="vigenere">Vigenere</option>
                <option value="playfair">Playfair</option>
                <option value="affine">Affine</option>
                <option value="hill">Hill</option>
            </select>
            <div className="cipher-input">
                {
                    cipher === 'vigenere' ? (
                        <div className="vigenere">
                            <div className="cipher-input-data">
                                <p>Type</p>
                                <input type="radio" name="v_type" id="v_standard" value="v_standard" defaultChecked/>
                                <label htmlFor="v_standard">Standard</label>
                                <input type="radio" name="v_type" id="v_full" value="v_full"/>
                                <label htmlFor="v_full">Full</label>
                                <input type="radio" name="v_type" id="v_auto" value="v_auto"/>
                                <label htmlFor="v_auto">Auto</label>
                                <input type="radio" name="v_type" id="v_extended" value="v_extended"/>
                                <label htmlFor="v_extended">Extended</label>
                                <p>Key</p>
                                <input type="text" name="vigenere_key" id="v_key"/>
                            </div>
                        </div>
                    ) : cipher === 'playfair' ? (
                        <div className="playfair">
                            <div className="cipher-input-data">
                                <p>Key</p>
                                <input type="text" name="playfair_key" id="p_key"/>
                            </div>
                        </div>
                    ) : cipher === 'affine' ? (
                        <div className="affine">
                            <div className="cipher-input-data">
                                <p>Key a: <input type="text" name="affine_key" id="a_key_a"/></p> 
                                <p>Key b: <input type="text" name="affine_key" id="a_key_b"/></p>                                
                            </div>
                        </div>
                    ) : cipher === 'hill' ? (
                        <div className="hill">
                            <div className="cipher-input-data">
                                <p>Key Matrix. Row is space separated. Column is newline separated</p>
                                <textarea name="hill_key" id="h_key" cols="30" rows="10"></textarea>
                            </div>
                        </div>
                    ) : null
                }
            </div>            
            <span className="gas-button" onClick={() => handleCipherSubmit()}>GAS</span>
            <div className="io-field">
                <p>Input Text</p>
                <textarea name="input-text" id="input-text" rows="10" onChange={(e) => setTextData(e.target.value)}></textarea>
            </div>
            <div className="io-field">
                <p>Output Text</p>
                <textarea name="input-text" id="input-text" rows="10"></textarea>
            </div>
        </Wrapper>
    )
}
const Wrapper = styled.div`
    padding-left: 1.5rem;
    display: flex;
    flex-direction: column;
    .io-field {
        margin-top: 1rem;
        textarea {
            width:100%;
        }
    }
    p {
        margin-block-end: 0;
        margin-block-start: 0;
    }
    option {
        padding: 5px;
    }
    .cipher-input {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .gas-button {
        padding: 10px;
        padding-top: 5px;
        padding-bottom: 5px;
        min-width: 100px;
        background-color: #1e9c66;
        color: white;
        border: 1px solid #0f6b44;
        border-radius: 5px;
    }
    .gas-button:hover {
        cursor: pointer;
        background-color: black;
    }
    .vigenere {
        input[type=radio] {
            margin-right: 5px;
        }
        label {
            margin-right: 2rem;
        }
    }
    
`;
export default CipherSelector
