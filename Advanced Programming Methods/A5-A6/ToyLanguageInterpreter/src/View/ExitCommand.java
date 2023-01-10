package View;

public class ExitCommand extends Command {
    public ExitCommand(String key, String description1) {
        super(key, description1);
    }

    @Override
    public void execute() {
        System.exit(0);
    }

}
