import React, { useState } from 'react';
import * as Survey from 'survey-react';
import 'survey-core/defaultV2.min.css';
import surveyJSON from './surveyData'; // Import the survey JSON file
import { Model } from "survey-core"; // Import Model from survey-core
import { BorderlessLight } from "survey-core/themes/borderless-light";

const SurveyComponent = () => {
    const surveyModel = new Model(surveyJSON);
    surveyModel.applyTheme(BorderlessLight);
    
    const [surveyResult, setSurveyResult] = useState(null);

    const onCompleteSurvey = (survey) => {
        // Get survey responses
        const surveyData = survey.data;

        // Send survey responses to the server
        fetch('http://localhost:8000/mainapp/save-data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(surveyData),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to submit survey');
            }
            return response.json();
        })
        .then(data => {
            // Handle successful response from server
            console.log('Survey submitted successfully:', data);
        })
        .catch(error => {
            // Handle errors
            console.error('Error submitting survey:', error);
        });
    };


    return (
        <div>
            <Survey.Survey model={surveyModel} onComplete={onCompleteSurvey} />
        </div>
    );
};

export default SurveyComponent;
