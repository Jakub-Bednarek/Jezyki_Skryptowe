import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.AbstractMap;

public class JavaCovid {
    private static final String DEFAULT_COVID_FILENAME = "Covid.txt";
    private static final String DEFAULT_COUNTRY = "Poland";
    private static final String DEFAULT_MONTH = "3";
    private static final int    DEFAULT_COUNTRY_INDEX = 6;
    private static final int    DEFAULT_MONTH_INDEX = 2;
    private static final int    DEFAULT_CASES_INDEX = 4;
    private static final int    EXPECTED_MINIMUM_TOKENS_IN_LINE = 11;
    private static final int    EXPECTED_ARGUMENTS_SIZE = 2;

    private static int extract_cases_from_line(final String line, final String month, final String country) {
        String[] tokens = line.split("\t");
        if(tokens.length < EXPECTED_MINIMUM_TOKENS_IN_LINE) {
            return 0;
        }

        int cases = 0;
        if(tokens[DEFAULT_MONTH_INDEX].equals(month) && tokens[DEFAULT_COUNTRY_INDEX].equals(country)){
            try {
                cases = Integer.parseInt(tokens[DEFAULT_CASES_INDEX]);
            } catch(NumberFormatException e) {}
        }

        return cases;
    }

    private static int get_all_cases(final String month, final String country) {
        int sum = 0;
        try(BufferedReader input = new BufferedReader(new FileReader(DEFAULT_COVID_FILENAME))) {
            for(String line; (line = input.readLine()) != null; ) {
                sum += extract_cases_from_line(line, month, country);
            }
        } catch(IOException e) { }

        return sum;
    }

    private static AbstractMap.SimpleEntry<String, String> parse_arguments(String[] args) {
        if(args.length == 0) {
            return new AbstractMap.SimpleEntry<>(DEFAULT_MONTH, DEFAULT_COUNTRY);
        }

        int month_pos = -1;
        for(int i = 0; i < args.length; i++) {
            try {
                Integer.parseInt(args[i]);
                month_pos = i;
            } catch(NumberFormatException e) {}
        }

        AbstractMap.SimpleEntry<String, String> month_and_country = null;
        if(args.length == 1) {
            if(month_pos == -1) {
                month_and_country = new AbstractMap.SimpleEntry<>(DEFAULT_MONTH, args[0]);
            } else {
                month_and_country = new AbstractMap.SimpleEntry<>(args[0], DEFAULT_COUNTRY);
            }
        } else {
            month_and_country = new AbstractMap.SimpleEntry<>(args[month_pos], args[EXPECTED_ARGUMENTS_SIZE - (month_pos + 1)]);
        }

        return month_and_country;
    }

    public static void main(String[] args) {
        AbstractMap.SimpleEntry<String, String> month_and_country = parse_arguments(args);
        System.out.println(get_all_cases(month_and_country.getKey(), month_and_country.getValue()));
    }
}