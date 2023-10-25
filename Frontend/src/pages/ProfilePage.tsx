import React from "react";
import { TextField, Box, Button, Paper, Typography } from "@mui/material";
import useChangeMailRPC from "@hooks/backend/userService/useChangeMailRPC";
import useResetPasswordRPC from "@hooks/backend/userService/useResetPasswordRPC";
import { useTranslation } from "react-i18next";

const ProfilePage = () => {
  const { changeMail } = useChangeMailRPC();
  const { resetPassword } = useResetPasswordRPC();
  const [email, setEmail] = React.useState<string>("");
  const [password, setPassword] = React.useState<string>("");
  const [submitted, setSubmitted] = React.useState<boolean>(false);
  const [submittedEmail, setSubmittedEmail] = React.useState<boolean>(false);
  const { t } = useTranslation();

  const changePassword = React.useCallback(
    async (e) => {
      e.preventDefault();

      try {
        await resetPassword(password);
        setSubmitted(true);
      } catch (error) {
        console.error(error);
      }
    },
    [password, setSubmitted],
  );

  const changeEmail = React.useCallback(
    async (e) => {
      e.preventDefault();
      try {
        await changeMail(email);
        setSubmittedEmail(true);
      } catch (error) {
        console.error(error);
      }
    },
    [email, setSubmitted],
  );

  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "calc(100vh - 110px)",
      }}
    >
      <Paper sx={{ p: 2, width: "25em" }}>
        <Box
          component="form"
          sx={{
            display: "flex",
            flexDirection: "column",
            gap: 2,
            marginBottom: 4,
          }}
          onSubmit={changePassword}
        >
          <Typography variant="h6">
            {t("profilePage.passwordChange")}
          </Typography>
          {submitted && (
            <Typography>{t("profilePage.resetEmailSent")}</Typography>
          )}
          {!submitted && (
            <>
              <TextField
                type="password"
                name="password"
                label={t("profilePage.newPassword")}
                value={password}
                required
                onChange={(e) => setPassword(e.target.value)}
              />
              <Button type="submit" variant="contained" color="primary">
                {t("profilePage.resetPassword")}
              </Button>
            </>
          )}
        </Box>
        <Box
          component="form"
          sx={{ display: "flex", flexDirection: "column", gap: 2 }}
          onSubmit={changeEmail}
        >
          <Typography variant="h6">{t("profilePage.emailChange")}</Typography>
          {submittedEmail && (
            <Typography>{t("profilePage.emailUpdated")}</Typography>
          )}
          {!submittedEmail && (
            <>
              <TextField
                name="email"
                label={t("profilePage.newEmail")}
                value={email}
                required
                onChange={(e) => setEmail(e.target.value)}
              />
              <Button type="submit" variant="contained" color="primary">
                {t("profilePage.validate")}
              </Button>
            </>
          )}
        </Box>
      </Paper>
    </Box>
  );
};

export default ProfilePage;
