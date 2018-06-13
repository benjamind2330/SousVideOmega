package industries.o.b.sousvideapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    public static final String EXTRA_MESSAGE = "industries.o.b.sousvideapp.MESSAGE";

    // Used to load the 'native-lib' library on application startup.
    static {
        System.loadLibrary("native-lib");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Example of a call to a native method
        //TextView tv = (TextView) findViewById(R.id.sample_text);
        //tv.setText(stringFromJNI());


        TextView temp = (TextView)findViewById(R.id.textViewTemperature);
        temp.setText("0.0");

        SV_comms.connect();

        SV_comms.start();

        final ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor();
        executorService.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                updateViews();
            }
        }, 0, 200, TimeUnit.MILLISECONDS);

    }

    private void updateViews() {
        SousVideCommunications.SousVideStatus stat = SV_comms.get_currentStatus();
        TextView temp = (TextView)findViewById(R.id.textViewTemperature);
        temp.setText(Float.toString(stat.temperature));
    }


    private SousVideCommunications SV_comms = new SousVideCommunications();

    /**
     * A native method that is implemented by the 'native-lib' native library,
     * which is packaged with this application.
     */
    public native String stringFromJNI();
}
