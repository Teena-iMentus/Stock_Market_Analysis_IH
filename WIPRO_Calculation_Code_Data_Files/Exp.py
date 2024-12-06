# Initialize the counter for unmatched defense levels outside the loop
unmatched_defense_counter = 0

if row['BuyersInControlPrice'] != 0:
    # Defence Check
    low_future_rows = df.iloc[i+1:]['Low']
    matched_low_index = low_future_rows[low_future_rows == defence].index
    
    if not matched_low_index.empty:
        matched_low_index = matched_low_index[0]
        max_high = df.loc[i:matched_low_index, 'High'].max()
        max_close = df.loc[i:matched_low_index, 'Close'].max()

        df.loc[i, f'PIT_Target_Buyer_{percent}'] = max_close
        df.loc[i, f'PIT_Aggresive_T_{percent}'] = max_high
    else:
        # Increment the counter when matched_low_index is empty
        unmatched_defense_counter += 1
        # Print the counter value for tracking during the loop
        print(f"Unmatched defense count so far: {unmatched_defense_counter}")

# Print the total count after the entire DataFrame processing
print(f"Total number of times matched_low_index was empty: {unmatched_defense_counter}")
