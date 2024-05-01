const surveyJSON = {
  title: "Mental Health assessment",
  showTOC: "true",
  showProgressBar: "top",
  pages: [
    {
      name: "Demographic Deets",
      elements: [
        { type: "text", name: "age", title: "Respondent age", isRequired: false },
        { type: "radiogroup", name: "gender", title: "Respondent gender", isRequired: false, choices: ["Male", "Female", "Other"] },
        { type: "text", name: "country", title: "Respondent country", isRequired: false },
        { type: "text", name: "state", title: "If you live in the United States, which state or territory do you live in?" }
      ]
    },
    {
      name: "Employment conditions",
      elements: [
        { type: "radiogroup", name: "self_employed", title: "Are you self-employed?", isRequired: false, choices: ["Yes", "No"] },
        { type: "radiogroup", name: "family_history", title: "Do you have a family history of mental illness?", isRequired: false, choices: ["Yes", "No"] },
        { type: "radiogroup", name: "treatment", title: "Have you sought treatment for a mental health condition?", isRequired: false, choices: ["Yes", "No"] },
        { type: "radiogroup", name: "work_interfere", title: "If you have a mental health condition, do you feel that it interferes with your work?", isRequired: false, choices: ["Never", "Rarely", "Sometimes", "Often"] },
        { type: "radiogroup", name: "no_employees", title: "How many employees does your company or organization have?", isRequired: false, choices: ["6-25", "More than 1000", "26-100", "100-500", "1-5", "500-1000"] },
        { type: "radiogroup", name: "remote_work", title: "Do you work remotely (outside of an office) at least 50% of the time?", isRequired: false, choices: ["Yes", "No"] },
        { type: "radiogroup", name: "tech_company", title: "Is your employer primarily a tech company/organization?", isRequired: false, choices: ["Yes", "No"] },
        { type: "radiogroup", name: "benefits", title: "Does your employer provide mental health benefits?", isRequired: false, choices: ["Yes", "No", "Don't know"] },
        { type: "radiogroup", name: "care_options", title: "Do you know the options for mental health care your employer provides?", isRequired: false, choices: ["Yes", "No", "Not sure"] },
        { type: "radiogroup", name: "wellness_program", title: "Has your employer ever discussed mental health as part of an employee wellness program?", isRequired: false, choices: ["Yes", "No", "Don't know"] },
        { type: "radiogroup", name: "seek_help", title: "Does your employer provide resources to learn more about mental health issues and how to seek help?", isRequired: false, choices: ["Yes", "No", "Don't know"] },
        { type: "radiogroup", name: "anonymity", title: "Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment?", isRequired: false, choices: ["Yes", "No", "Don't know"] },
        { type: "radiogroup", name: "leave", title: "How easy is it for you to take medical leave for a mental health condition?", isRequired: false, choices: ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult","Don't know"] }
      ]
    },
    {
      name: "Workplace Attitudes",
      elements: [
        { type: "radiogroup", name: "mental_health_consequence", title: "Do you think that discussing a mental health issue with your employer would have negative consequences?", isRequired: false, choices: ["No", "Maybe", "Yes"] },
        { type: "radiogroup", name: "phys_health_consequence", title: "Do you think that discussing a physical health issue with your employer would have negative consequences?", isRequired: false, choices: ["No", "Maybe", "Yes"] },
        { type: "radiogroup", name: "coworkers", title: "Would you be willing to discuss a mental health issue with your coworkers?", isRequired: false, choices: ["No", "Some of them", "Yes"] },
        { type: "radiogroup", name: "supervisor", title: "Would you be willing to discuss a mental health issue with your direct supervisor(s)?", isRequired: false, choices: ["No", "Some of them", "Yes"] },
        { type: "radiogroup", name: "mental_health_interview", title: "Would you bring up a mental health issue with a potential employer in an interview?", isRequired: false, choices: ["No", "Maybe", "Yes"] },
        { type: "radiogroup", name: "phys_health_interview", title: "Would you bring up a physical health issue with a potential employer in an interview?", isRequired: false, choices: ["No", "Maybe", "Yes"] },
        { type: "radiogroup", name: "mental_vs_physical", title: "Do you feel that your employer takes mental health as seriously as physical health?", isRequired: false, choices: ["No", "Don't know", "Yes"] },
        { type: "radiogroup", name: "obs_consequence", title: "Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?", isRequired: false, choices: ["No", "Yes"] }
      ]
    },
    {
      name: "Misc",
      elements: [
        { type: "comment", name: "comments", title: "Any additional notes or comments?" }
      ]
    }
  ]
};

// const surveyJSON = {
//   pages: [{
//     name: "Name",
//     elements: [{
//       name: "FirstName",
//       title: "Enter your first name:",
//       type: "text"
//     }, {
//       name: "LastName",
//       title: "Enter your last name:",
//       type: "text"
//     }]
//   }]
// };
//this is a sample

export default surveyJSON;

