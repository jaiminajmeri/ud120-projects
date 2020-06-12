#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    errors = predictions - net_worths
    errors.sort(axis=0)
    
    len_pred = len(predictions)
    th_index = ( len_pred - ( (len_pred * 10) / 100 ) ) - 1
    err_th = errors[th_index]

    ### your code goes here
    for i in range(0, len(predictions)):
        error = predictions[i] - net_worths[i]
        if error <= err_th:
            value = (ages[i], net_worths[i], error)
            cleaned_data.append(value)
    
    print "New Length:", len(cleaned_data)
    return cleaned_data

