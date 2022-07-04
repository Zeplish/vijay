def result_message(mess):
    if mess == "predict":
        return "This page displays the results of the Predict Module for the query sequence(s) submitted by the user. The table below shows the details of the query peptide sequence(s), with the first column displaying the serial number of the input peptide sequence, the second column displaying the ID of the submitted input sequence, the third column representing the sequence of the submitted peptide, the fourth column displaying the probability score of the given peptide being IL-13 inducer. The last column displays the prediction of whether the peptide might have IL-13 induction activity or not as determined by the condition of whether the probability score is greater or less than the user-defined threshold."
    elif mess == "protein":
        return "This page displays the results of the protein scan module of the query protein. The table below shows the details of the query protein sequence, with the first column displaying the serial number, the second column displaying the ID of the peptide fragment, the third column displaying the sequence of the generated peptide, the fourth column displaying the IL-13 induction probability of given peptide as provided by the machine learning algorithm. The last column displays the prediction of whether the peptide might have IL-13 induction activity or not as determined by the condition whether the probability score is greater or less than the user-defined threshold."

    elif mess == "design":
        return "This page displays the results of the design module in the single substitution mutants of the query peptide. The table below shows the details of the query peptide sequences, with the first column displaying the serial number, the second column displaying the ID of the mutant sequence, the third column displaying the sequence of the mutant generated, the fourth column displaying the probability provided by the machine learning algorithm. The last column displays the prediction of whether a peptide and it's mutant might have IL-13 induction activity or not as determined by the condition whether the probability score is greater or less than the user-defined threshold."


def result_title(mess):
    if mess == "predict":
        return "Result of Predict Module"
    elif mess == "protein":
        return "Result of Protein Scan Module"

    elif mess == "design":
        return "Result of Design Module"

def error_message(mess):
    if mess == "404":
        return "oops!! Page not found 404!!"
    elif mess == "500":
        return "oops!! Something Went Wrong!!"

def error_title(mess):
    if mess =="404":
        return "404"
    elif mess =="500":
        return "500"