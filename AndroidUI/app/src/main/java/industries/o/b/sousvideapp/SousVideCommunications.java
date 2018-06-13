package industries.o.b.sousvideapp;

import android.util.Log;

import java.util.concurrent.TimeUnit;
import org.zeromq.ZMQ;
import org.zeromq.ZContext;


public class SousVideCommunications extends Thread {

    public class SousVideStatus {
        public float temperature = 0.0f;
    }


    private ZMQ.Context context;
    ZMQ.Socket subscriber;

    public void connect() {

        context = ZMQ.context(1);

        //  Socket to talk to server
        subscriber = context.socket(ZMQ.SUB);
        subscriber.connect("tcp://192.168.1.133:5556");

        subscriber.subscribe("");
    }


    public void run() {
        while (!_shutdown) {

            String string = subscriber.recvStr(0).trim();
            Log.d("COMMS", string);
            synchronized (_statlock) {
                _currentStatus.temperature++;
            }
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (java.lang.InterruptedException e) {

            }
        }
    }

    public SousVideStatus get_currentStatus() {
        synchronized (_statlock) {
            return _currentStatus;
        }
    }

    private Object _statlock = new Object();
    private SousVideStatus _currentStatus = new SousVideStatus();
    private Boolean _shutdown = false;


}
