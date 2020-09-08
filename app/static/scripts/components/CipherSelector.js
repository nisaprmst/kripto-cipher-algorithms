import React, { useState } from 'react'
import styled from 'styled-components';
const CipherSelector = () => {
    const [cipher, setCipher] = useState('vigenere');

    const handleCipherSelected = (selectEl) => {
        const val = selectEl.options[selectEl.selectedIndex].value;
        setCipher(val);
    };
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
                                <input type="radio" name="v_type" id="v_standard"/>
                                <label htmlFor="v_standard">Standard</label>
                                <input type="radio" name="v_type" id="v_full"/>
                                <label htmlFor="v_full">Full</label>
                                <input type="radio" name="v_type" id="v_auto"/>
                                <label htmlFor="v_auto">Auto</label>
                                <input type="radio" name="v_type" id="v_extended"/>
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
                                <p>Key a: <input type="text" name="affine_key" id="p_key_a"/></p> 
                                <p>Key b: <input type="text" name="affine_key" id="p_key_b"/></p>                                
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
            <span className="gas-button">GAS</span>
        </Wrapper>
    )
}
const Wrapper = styled.div`
    padding-left: 1.5rem;
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
