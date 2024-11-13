const ws = new WebSocket("ws://technest.ddns.net:8001/ws");

ws.onopen = () => {
    console.log("WebSocket connection opened successfully.");
    
    // ส่ง API Key หลังจากเชื่อมต่อ WebSocket สำเร็จ
    const authMessage = {
        action: "authenticate",   // กำหนด action ว่าเป็นการ authentication
        api_key: "670a935a14221a12ae886117c99cacc7"  // API Key ของคุณ
    };
    
    // ส่งข้อความที่มี API Key ไปยังเซิร์ฟเวอร์
    ws.send(JSON.stringify(authMessage));
};

ws.onmessage = (event) => {
    console.log("Data received from WebSocket:", event.data);
    try {
        const message = JSON.parse(event.data);
        
        // ตัวอย่างการใช้งานข้อมูลที่รับมาจาก WebSocket
        const timestamp = new Date();
        const value = message.data;

        // สมมุติว่า WebSocket ส่งข้อมูลที่มีค่า "data"
        if (value !== undefined) {
            chartData.labels.push(timestamp);
            chartData.datasets[0].data.push(value);

            // จำกัดจำนวนจุดข้อมูลที่แสดงในกราฟ
            if (chartData.labels.length > dataLimit) {
                chartData.labels.shift();
                chartData.datasets[0].data.shift();
            }

            machineDataChart.update();
        } else {
            console.warn("Received message does not have 'data' field:", message);
        }
    } catch (error) {
        console.error("Error parsing WebSocket data:", error);
    }
};

ws.onerror = (error) => {
    console.error("WebSocket Error:", error);
    document.getElementById('error-message').innerText = "Failed to connect to WebSocket.";
};

ws.onclose = () => {
    console.log("WebSocket connection closed.");
    document.getElementById('error-message').innerText = "Connection to WebSocket closed.";
};
