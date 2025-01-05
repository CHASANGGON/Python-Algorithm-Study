import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Player implements Comparable<Player> {
    int level;
    String nickname;

    public Player(int level, String nickname) {
        this.level = level;
        this.nickname = nickname;
    }

    // 닉네임 기준 사전순 정렬
    @Override
    public int compareTo(Player other) {
        return this.nickname.compareTo(other.nickname);
    }
}

class Room {
    int minLevel;
    int maxLevel;
    int maxPlayers; // 방의 정원
    List<Player> players = new ArrayList<>(); // 플레이어 리스트

    // 생성자
    public Room(int level, int maxPlayers) {
        this.minLevel = level - 10;
        this.maxLevel = level + 10;
        this.maxPlayers = maxPlayers;
    }

    // 입장 여부 체크 메서드
    public boolean canJoin(Player player) {
        return player.level >= minLevel && player.level <= maxLevel && players.size() < maxPlayers;
    }

    // 플레이어 추가
    public void addPlayer(Player player) {
        players.add(player);
    }

    // 방이 꽉 찼는지 확인하는 메서드
    public boolean isFull() {
        return players.size() == maxPlayers;
    }

    // 방의 상태를 출력하는 메서드
    public void printRoomStatus() {
        Collections.sort(players); // 닉네임 기준 플레이어 정렬
        if (isFull()) {
            System.out.println("Started!");
        } else {
            System.out.println("Waiting!");
        }
        for (Player player : players) {
            System.out.println(player.level + " " + player.nickname);
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // p, m 입력 받기
        String[] pm = br.readLine().split(" ");
        int p = Integer.parseInt(pm[0]);
        int m = Integer.parseInt(pm[1]);

        List<Room> rooms = new ArrayList<>(); // 방 리스트

        for (int i = 0; i < p; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int level = Integer.parseInt(st.nextToken());
            String nickname = st.nextToken();
            Player newPlayer = new Player(level, nickname);

            boolean isJoined = false;
            // 기존 방을 순회하며 입장 가능한 방 찾기
            for (Room room : rooms) {
                if (room.canJoin(newPlayer)) {
                    room.addPlayer(newPlayer);
                    isJoined = true;
                    break;
                }
            }

            // 입장 가능한 방이 없으면 새로운 방 생성
            if (!isJoined) {
                Room newRoom = new Room(level, m);
                newRoom.addPlayer(newPlayer);
                rooms.add(newRoom);
            }
        }

        // 입력이 끝나고 모든 방의 상태 출력
        for (Room room : rooms) {
            room.printRoomStatus();
        }
    }
}
