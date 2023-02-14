Build a visualisation similar to the [GitHub contributions calendar](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/viewing-contributions-on-your-profile#contributions-calendar) graphing the daily price spread (difference between high and low price) for the USD/BTC exchange rate.

### Visualisation:

- Each day in the graph is represented as a single square
- For a given day, spread is defined as: *spread = max price – min price*
- The graph should display USD/BTC price spreads for each day over a time period of 1 year

The colour of each square should be determined as follows:
- The highest spread value in the time period should be a dark orange square: rgb(255, 76, 0)
- The lowest spread value in the time period should be a light orange square: rgb(255, 246, 235)
- Spread values between the highest and lowest should follow a linear colour gradient

### Solution requirements:

- The tool should support parametrization to allow viewing data from previous years
- BTC price data may be obtained from any available 3rd party API. Any available USD/BTC exchange rate is allowed
- The full source code for the project should be provided with installation instructions for required dependencies to run the visualisation tool
- An example output from the tool should be provided as an image file in the repository
- Describe how the visualisation tool works and how to obtain up-to-date data in a README.md file.
- Please provide the project in a public git repository.

Please also make sure to send the result of your coding task also to my colleague in the CC. Thereby we make sure that your coding task will find us well in case I won't be available myself.
