package com.example.edu_connect_backend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public User registerUser(User user) {
        // Проверка, существует ли пользователь с таким email
        if (userRepository.findByEmail(user.getEmail()) != null) {
            throw new UserAlreadyExistsException("Пользователь с таким email уже зарегистрирован");
        }
        return userRepository.save(user);
    }

    public User loginUser(String email, String password) {
        User foundUser = userRepository.findByEmail(email);
        if (foundUser == null || !foundUser.getPassword().equals(password)) {
            throw new InvalidCredentialsException("Неверный email или пароль");
        }
        return foundUser;
    }

    public void changePassword(String email, String currentPassword, String newPassword) {
        User user = userRepository.findByEmail(email);
        if (user == null) {
            throw new InvalidCredentialsException("Пользователь с таким email не найден");
        }

        // Проверяем текущий пароль
        if (!user.getPassword().equals(currentPassword)) {
            throw new InvalidCredentialsException("Неверный текущий пароль");
        }

        // Устанавливаем новый пароль
        user.changePassword(newPassword);
        userRepository.save(user);
    }

    public User getUserById(String id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Пользователь с id " + id + " не найден"));
    }
}